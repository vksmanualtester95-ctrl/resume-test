#!/usr/bin/env python3
"""
gap.py - Compares your resume against a job description.

Tells you: which required skills are missing, which acronyms you wrote in only
one form, and how well your title matches. No invented "match score" - it only
counts real words.

Usage:
  python3 scripts/gap.py output/resume.pdf jobs/acme/jd.txt
"""
import argparse, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import read_any  # noqa: E402

# Words that are never a skill, so they never count as a "gap".
NOISE = set("""
a an the and or of to in for with on at by as is are was were be been from that this it its
we you our us their they them who whom which will shall may might must can could would should
about above after again against all any because before being below between both but did do does
doing down during each few further had has have having here how into more most no nor not off
once only other out over own same so some such than then there these those through too under
until up very what when where while why work working works role position candidate candidates
applicant company team teams year years experience strong excellent good great new using use
used help helps helping join joining opportunity responsibilities requirements qualifications
preferred required plus bonus nice must have haves benefits salary apply application job
description looking seeking ability able across ensure ensuring including include includes
build building develop developing design designing manage managing support supporting deliver
delivering create creating maintain maintaining implement implementing understand knowledge
skills skill environment environments solution solutions business technical related field
degree bachelor master equivalent minimum least etc via per within upon end high low well
proven title location hybrid remote onsite office senior junior lead principal staff associate
large-scale scale scalable database databases advanced strong deep expert hands own owning
mentor mentoring junior improve improving reliability compliance optimization cost platform
familiarity exposure preferred plus good nice must required
""".split())

MUST_RE = re.compile(r"\b(must have|must|required|requirement|minimum|at least|mandatory|"
                     r"essential|proven|hands[- ]on|you have|we require)\b", re.I)
NICE_RE = re.compile(r"\b(nice to have|preferred|plus|bonus|desirable|good to have|"
                     r"advantage|familiarity|exposure|a plus)\b", re.I)
TITLE_RE = re.compile(r"^\s*(?:job title|title|position|role)\s*[:\-]\s*(.+)$", re.I | re.M)
YEARS_RE = re.compile(r"(\d{1,2})\s*\+?\s*(?:years?|yrs?)", re.I)

ACRONYMS = {
    "adf": "azure data factory", "adls": "azure data lake storage",
    "etl": "extract transform load", "elt": "extract load transform",
    "ci/cd": "continuous integration", 
    "ml": "machine learning", 
    "llm": "large language model", "rag": "retrieval augmented generation",
    "nlp": "natural language processing", "bi": "business intelligence",
    "aws": "amazon web services", "gcp": "google cloud platform",
    "k8s": "kubernetes", "iac": "infrastructure as code",
    "api": "application programming interface", "sla": "service level agreement",
    "rbac": "role based access control", "dwh": "data warehouse",
    "kpi": "key performance indicator", 
    "gcc": "global capability center", 
     "mdm": "master data management",
    "cdc": "change data capture", 
}


def words(s):
    return re.findall(r"[A-Za-z][A-Za-z0-9+#./_\-]*", s)


def norm(s):
    return re.sub(r"\s+", " ", s.lower())


def jd_terms(jd):
    """Pull likely SKILL terms out of a JD, not every English word."""
    terms = {}
    # 1. Capitalised words / acronyms / things with digits or punctuation.
    #    Real skills look like: Azure, PySpark, ADF, CI/CD, Python3, .NET, dbt
    for w in words(jd):
        lw = w.lower().strip(".,;:")
        if len(lw) < 2 or lw in NOISE:
            continue
        looks_like_skill = (
            w[0].isupper()                       # Azure, Databricks
            or w.isupper()                       # ADF, ETL, SQL
            or any(c.isdigit() for c in w)       # Gen2, Python3
            or any(c in w for c in "+#./_-")     # CI/CD, C#, .NET, dbt-core
        )
        if looks_like_skill:
            terms[lw] = terms.get(lw, 0) + 1
    # 2. Two-word phrases where BOTH words are capitalised in the original.
    for m in re.finditer(r"\b([A-Z][a-zA-Z0-9]+)\s+([A-Z][a-zA-Z0-9]+)\b", jd):
        p = f"{m.group(1).lower()} {m.group(2).lower()}"
        if not any(x in NOISE for x in p.split()):
            terms[p] = terms.get(p, 0) + 2      # phrases weigh more
    return terms


def resume_surface(txt):
    t = norm(txt)
    s = set(w.lower().strip(".,;:") for w in words(txt))
    for i, w in enumerate(words(txt)[:-1]):
        s.add(f"{w.lower()} {words(txt)[i+1].lower()}")
    for a, e in ACRONYMS.items():
        if a in s:
            s.add(e)
        if e in t:
            s.add(a)
    return s, t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("resume")
    ap.add_argument("jd")
    ap.add_argument("--top", type=int, default=25)
    a = ap.parse_args()
    for p in (a.resume, a.jd):
        if not os.path.exists(p):
            sys.exit(f"not found: {p}")

    rtext, _ = read_any(a.resume)
    jd = open(a.jd, encoding="utf-8", errors="replace").read()
    have, rlow = resume_surface(rtext)

    # which JD lines state a MUST vs a NICE
    must_words, nice_words = set(), set()
    for line in jd.splitlines():
        ln = line.strip(" \t-*\u2022")
        if len(ln) < 8:
            continue
        bucket = nice_words if NICE_RE.search(ln) else (must_words if MUST_RE.search(ln) else None)
        if bucket is not None:
            bucket.update(k for k in jd_terms(ln))

    terms = jd_terms(jd)
    ranked = sorted(terms.items(), key=lambda kv: -kv[1])

    covered, missing = [], []
    for term, freq in ranked:
        hit = term in have
        if not hit and " " not in term and len(term) > 4:
            hit = any(h.startswith(term[:max(4, len(term) - 2)]) for h in have)
        (covered if hit else missing).append(term)

    total = len(covered) + len(missing)
    cov = round(100 * len(covered) / total) if total else 0
    band = ("critical" if cov < 50 else "borderline" if cov < 70
            else "good" if cov < 85 else "strong")

    phrases = {t for t in missing if " " in t}
    inside = {w for p_ in phrases for w in p_.split()}
    missing = [t for t in missing if " " in t or t not in inside]

    must_missing = [t for t in missing if t in must_words][:a.top]
    nice_missing = [t for t in missing if t in nice_words and t not in must_words][:12]
    other_missing = [t for t in missing if t not in must_words and t not in nice_words][:18]

    acro = []
    for s, l in ACRONYMS.items():
        in_jd = re.search(rf"\b{re.escape(s)}\b", jd, re.I) or l in norm(jd)
        if not in_jd:
            continue
        has_s = bool(re.search(rf"\b{re.escape(s)}\b", rtext, re.I))
        has_l = l in rlow
        if (has_s or has_l) and not (has_s and has_l):
            acro.append(f"{s.upper()} / {l}  ->  write it once as "
                        f"\"{l.title()} ({s.upper()})\"")

    m = TITLE_RE.search(jd)
    title = m.group(1).strip() if m else (jd.strip().splitlines() or [""])[0][:70]
    ttok = {w.lower() for w in words(title) if w.lower() not in NOISE}
    tcov = round(100 * len(ttok & have) / len(ttok)) if ttok else 0
    yrs = YEARS_RE.findall(jd)

    print("=" * 72)
    print(f" JD GAP  |  {title[:58]}")
    print("=" * 72)
    print(f" Skill-term coverage : {cov}%  ({band})")
    print(f" Title alignment     : {tcov}%")
    if yrs:
        print(f" Experience asked    : {max(int(y) for y in yrs)}+ years")
    print("-" * 72)
    if must_missing:
        print(" MISSING - stated as REQUIRED (fix first, only if true for you):")
        for t in must_missing:
            print(f"   !  {t}")
    if nice_missing:
        print(" MISSING - preferred / nice to have:")
        print("      " + ", ".join(nice_missing))
    if other_missing:
        print(" MISSING - other JD vocabulary worth mirroring:")
        print("      " + ", ".join(other_missing))
    if acro:
        print(" ACRONYM MISMATCH (recruiters Boolean-search both forms):")
        for x in acro[:8]:
            print(f"   ~  {x}")
    if not (must_missing or nice_missing or other_missing or acro):
        print(" No meaningful gaps found.")
    print("-" * 72)
    print(" Add a term ONLY if you can talk about it for 90 seconds unprepared.")
    print(" A keyword that wins the screen and loses the interview is worse than none.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
