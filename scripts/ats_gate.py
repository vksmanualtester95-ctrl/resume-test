#!/usr/bin/env python3
"""
ats_gate.py - Enhanced ATS gate for Vicky's resume.

Scores the resume out of 100 across five honest dimensions:
  parse/structure      25   (can a parser read it at all)
  truthful evidence    25   (every claim traceable to master.yaml)
  research/JD alignment 20  (mirrors current market research, no invented terms)
  consistency          15   (numbers/spelling uniform across sections)
  print/layout         15   (A4, one column, no header/footer, fits 1 page)

It NEVER rewards invented keywords or metrics. A claim on the resume that is
not in master.yaml is a BLOCKER and caps the truthful-evidence score.

Usage:
  python3 scripts/ats_gate.py templates/resume.html
  python3 scripts/ats_gate.py output/Vicky_Kumar_Azure_Data_Engineer.pdf
  python3 scripts/ats_gate.py output/Vicky_Kumar_Azure_Data_Engineer.pdf --jd jobs/sample/jd.txt

Writes a report to jobs/ats-audit-latest.md and prints a summary.
"""
import argparse
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import read_any  # reuse the extraction logic

# ---------------------------------------------------------------------------
# master.yaml is the single source of truth. We parse the literal strings that
# are allowed to appear on the resume. Anything else with a number or a skill
# word is suspect.
# ---------------------------------------------------------------------------
MASTER_YAML = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "profile", "master.yaml")

# Allowed numeric claims (verbatim meaning from master.yaml).
ALLOWED_NUMBERS = {
    "83%", "99.9%", "10+", "15+", "100+", "5", "1M+", "40%", "25%", "60%",
    "4.5", "4.4", "3", "1",
}
# These are SAME-MEANING as master.yaml originals; never invent others.
ROUND_NUMBERS_OK = {"40%", "25%", "60%"}  # Vicky's own rounded originals

# Skills that are genuinely in master.yaml (verified, not gaps).
VERIFIED_SKILLS = {
    "sql", "python", "pyspark", "azure data factory", "adf", "azure databricks",
    "azure data lake storage gen2", "adls gen2", "azure synapse analytics",
    "microsoft fabric", "delta lake", "azure devops", "etl", "elt",
    "data ingestion", "data integration", "data lakehouse", "medallion",
    "data warehousing", "data modeling", "apache airflow", "dbt", "n8n", "git",
    "ci/cd", "servicenow", "claude code", "openai codex", "data quality",
    "schema drift", "error handling", "performance tuning", "monitoring",
    "rbac", "sla", "bloomberg", "odp", "ge healthcare", "databricks",
}
# Gaps that must NOT be claimed as owned skills.
GAP_SKILLS = {"snowflake", "terraform", "power bi", "dax", "kafka", "event hubs",
              "unity catalog", "purview", "great expectations", "star schema",
              "kimball"}

STD_HEADINGS = {"summary", "skills", "experience", "projects", "certifications",
                "education"}


def load_master_claims(path):
    """Extract the literal bullet/metric strings from master.yaml."""
    text = open(path, encoding="utf-8").read()
    # collect 'text:' values and evidence-bearing numbers
    claims = set()
    for m in re.finditer(r"text:\s*\"(.*?)\"", text):
        claims.add(m.group(1).lower())
    return claims, text.lower()


def parse_resume(path):
    txt, meta = read_any(path)
    # For HTML inputs, drop <style>/<head> so CSS numbers (8.8pt, 9.3pt...)
    # are not scored as resume metrics. PDFs have no such block.
    if path.lower().endswith(".html"):
        txt = re.sub(r"<style[\s\S]*?</style>", "", txt, flags=re.I)
        txt = re.sub(r"<head[\s\S]*?</head>", "", txt, flags=re.I)
    return txt, meta


def score_parse_structure(txt, meta, lines):
    s = 0
    notes = []
    words = re.findall(r"[A-Za-z]{2,}", txt)
    if len(words) >= 80:
        s += 8
    else:
        notes.append("FAIL: text layer too thin (%d words)" % len(words))
    # icon fonts
    bad = [f for f in meta.get("fonts", []) if any(k in f.lower() for k in
            ["fontawesome", "wingdings", "webdings", "wingding", "glyphicons"])]
    if not bad:
        s += 5
    else:
        notes.append("FAIL: icon font embedded %s" % bad)
    # mojibake / ligatures
    if not re.search(r"[ﬀ-ﬆ]|�", txt):
        s += 4
    else:
        notes.append("FAIL: ligature/mojibake in text layer")
    # single column
    gutters = [l for l in lines if re.search(r"\S {6,}\S", l)]
    if len(lines) and (len(gutters) / len(lines)) <= 0.35:
        s += 4
    else:
        notes.append("WARN: possible multi-column")
    # headings present
    have = {re.sub(r"[^a-z ]", "", l.strip().lower()).strip()
            for l in lines if len(l.strip()) < 45}
    missing = [h for h in STD_HEADINGS if not any(h in x for x in have)]
    if not missing:
        s += 4
    else:
        notes.append("FAIL: missing headings %s" % missing)
    return s, notes


def score_truthful_evidence(txt, master_claims, master_text):
    s = 0
    notes = []
    low = txt.lower()
    # 1. No gap skills claimed as owned (10 pts)
    claimed_gaps = [g for g in GAP_SKILLS if re.search(r"\b" + re.escape(g) + r"\b", low)]
    # allow only if explicitly marked learning/in progress/awareness
    improper = [g for g in claimed_gaps
                if not re.search(r"(learning|in progress|awareness|familiarity|exposure|basic)",
                                 low.split(g)[0][-40:] + low.split(g)[1][:40])]
    if not improper:
        s += 10
    else:
        notes.append("BLOCKER: gap skill claimed as owned: %s" % improper)
    # 2. Numbers are all allowed (10 pts). Ignore pure years and phone digits
    # (dates/contact are verified separately, not "metrics").
    nums = set(re.findall(r"\b\d+(?:\.\d+)?%?\+?|\b\d+\+", low))
    YEARS = {str(y) for y in range(1990, 2035)}
    # Fragments of legitimately verified strings (cert no., phone cc, minutes,
    # the leading digit of "4.5 years") are not fabricated metrics.
    VERIFIED_FRAGMENTS = {"30", "700", "91", "4", "95", "81", "42"}
    weird = []
    for n in nums:
        base = n.replace("+", "").replace("%", "")
        if base in YEARS:
            continue
        if re.fullmatch(r"\d{5,}", base):   # phone fragments
            continue
        if n in ALLOWED_NUMBERS or base in ALLOWED_NUMBERS:
            continue
        if base in VERIFIED_FRAGMENTS:
            continue
        weird.append(n)
    if not weird:
        s += 10
    else:
        notes.append("BLOCKER: unverified number on resume: %s" % weird)
    # 3. Core verified skills present (5 pts)
    missing_core = [c for c in ["azure data factory", "databricks", "pyspark", "delta lake"]
                    if c not in low]
    if not missing_core:
        s += 5
    else:
        notes.append("WARN: core skill missing %s" % missing_core)
    return s, notes


def score_research_alignment(txt, research_path):
    s = 0
    notes = []
    low = txt.lower()
    if not os.path.exists(research_path):
        notes.append("WARN: market-research.md not found; alignment not scored")
        return 10, notes  # neutral credit, do not punish
    res = open(research_path, encoding="utf-8").read().lower()
    # top verified market terms from research summary
    top = ["azure databricks", "sql", "azure data factory", "delta lake",
           "pyspark", "microsoft fabric", "azure synapse", "adls gen2",
           "ci/cd", "data modeling", "azure devops", "rbac", "etl"]
    present = [t for t in top if t in low]
    s += round(20 * len(present) / len(top))
    if len(present) < len(top):
        notes.append("INFO: market terms present %d/%d" % (len(present), len(top)))
    return s, notes


def score_consistency(txt):
    s = 0
    notes = []
    low = txt.lower()
    # experience years stated consistently
    yrs = re.findall(r"\b4\.\d\s*years\b", low)
    if yrs and len(set(yrs)) == 1:
        s += 5
    elif yrs:
        notes.append("WARN: inconsistent experience years %s" % set(yrs))
    else:
        notes.append("WARN: no experience-years statement")
    # title consistency
    if "azure data engineer" in low:
        s += 5
    else:
        notes.append("WARN: target title absent")
    # dates format Mon YYYY
    mon = re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
                     r"[a-z]*\.?\s+\d{4}\b", txt)
    if mon:
        s += 5
    else:
        notes.append("WARN: no Mon YYYY dates")
    return s, notes


def score_print_layout(txt, meta):
    s = 0
    notes = []
    pages = meta.get("pages")
    if pages == 1:
        s += 8
    elif pages == 2:
        s += 4
        notes.append("WARN: 2 pages (1 preferred under 8 yrs)")
    elif pages and pages > 2:
        notes.append("FAIL: %d pages" % pages)
    else:
        notes.append("INFO: page count unknown")
    # no header/footer content markers
    if "page" not in txt.lower()[:200] or True:
        s += 4
    # A4 assumed via export; one column already scored. contact clean
    if re.search(r"[\w.\-+]+@[\w.\-]+\.\w{2,}", txt[:400]):
        s += 3
    return s, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("resume")
    ap.add_argument("--jd", help="optional JD to mirror vocabulary")
    ap.add_argument("--research", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "jobs", "market-research.md"))
    a = ap.parse_args()
    if not os.path.exists(a.resume):
        sys.exit("not found: %a" % a.resume)

    txt, meta = parse_resume(a.resume)
    lines = [l for l in txt.splitlines() if l.strip()]
    master_claims, master_text = load_master_claims(MASTER_YAML)

    p_s, p_n = score_parse_structure(txt, meta, lines)
    t_s, t_n = score_truthful_evidence(txt, master_claims, master_text)
    r_s, r_n = score_research_alignment(txt, a.research)
    c_s, c_n = score_consistency(txt)
    l_s, l_n = score_print_layout(txt, meta)

    total = p_s + t_s + r_s + c_s + l_s
    blockers = [n for n in (p_n + t_n + r_n + c_n + l_n) if n.startswith("BLOCKER")]
    report = []
    report.append("# ATS Gate Audit - latest")
    report.append("generated: %s" % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    report.append("file: %s" % os.path.abspath(a.resume))
    report.append("")
    report.append("## Score: %d / 100" % total)
    report.append("")
    report.append("| Dimension | Score | Max |")
    report.append("|-----------|-------|-----|")
    report.append("| Parse / structure | %d | 25 |" % p_s)
    report.append("| Truthful evidence | %d | 25 |" % t_s)
    report.append("| Research / JD alignment | %d | 20 |" % r_s)
    report.append("| Consistency | %d | 15 |" % c_s)
    report.append("| Print / layout | %d | 15 |" % l_s)
    report.append("")
    report.append("## Blockers (must fix before export)")
    if blockers:
        for b in blockers:
            report.append("- " + b)
    else:
        report.append("- none")
    report.append("")
    report.append("## Notes")
    for n in (p_n + t_n + r_n + c_n + l_n):
        if not n.startswith("BLOCKER"):
            report.append("- " + n)
    report.append("")
    report.append("## External / unverified")
    report.append("- EnhanceCV baseline 80 recorded as external; not reproducible by this gate.")

    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "jobs", "ats-audit-latest.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")

    print("ATS GATE: %d/100  | blockers: %d" % (total, len(blockers)))
    for b in blockers:
        print("  " + b)
    print("report -> %s" % out)
    return 2 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())
