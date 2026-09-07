# Resume

ATS-safe, single-page resume for **Vicky Kumar — Azure Data Engineer**.
Built with HTML + CSS, exported to PDF via headless Chrome.

## Layout

```
profile/
  master.yaml                  # source of truth (no PII in this copy)
  master.local.yaml            # gitignored - phone/email override
  master.local.yaml.example    # schema reference for the override
  resume-style.yaml            # layout spec
scripts/
  check.py                     # ATS parsing audit
  gap.py                       # keyword-gap report vs a JD
  ats_gate.py
  merge_contact.py             # fills <!--PHONE--> / <!--EMAIL--> in HTML
templates/
  resume.html                  # the actual resume (has placeholders)
jobs/                          # JD analyses, market research, change log
input/  output/                # gitignored - source/final PDFs
.mcp.json                      # MCP servers used during research
CLAUDE.md                      # build rules
```

## First-time setup (on a new machine)

```bash
cp profile/master.local.yaml.example profile/master.local.yaml
# edit it with your real phone + email
python3 scripts/merge_contact.py        # fills the placeholders
```

## Build (local)

```bash
python3 scripts/merge_contact.py
python3 scripts/check.py templates/resume.html
python3 scripts/gap.py  templates/resume.html jobs/<jd>.txt   # optional
# Chrome > Cmd+P > Save as PDF (headers/footers OFF, scale 100%)
python3 scripts/check.py output/Vicky_Kumar_Azure_Data_Engineer.pdf
```

## Privacy

This repo is **private** but the same scrub rules apply if you ever
mirror or fork it:

- `profile/master.yaml` has **phone and email removed**
- `profile/master.local.yaml` (gitignored) holds the real values
- `templates/resume.html` uses `<!--PHONE-->` / `<!--EMAIL-->` placeholders
  that `merge_contact.py` fills at export time
- `input/` and `output/` PDFs are gitignored — they contain contact info
- `Profile Linkedin.pdf` is gitignored

See `CLAUDE.md` for the full build rules.
