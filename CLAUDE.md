# Resume project - rules

## Build Rules (Managed - do not edit between markers)
<!-- BEGIN MANAGED BUILD RULES -->
All resume builds MUST:
1. Read profile/resume-style.yaml for layout (header_unchanged, section gaps, role/project gaps, link style, A4, one-column, no header/footer, Chrome-only export)
2. Read jobs/market-research.md for current skill frequencies, recommended title, gaps, P0/P1/P2 actions
3. Read profile/master.yaml as the single source of truth for all facts
4. Run python3 scripts/check.py on the HTML before export
5. Run python3 scripts/gap.py against target JD if available
6. Export via Chrome headless to output/Vicky_Kumar_Azure_Data_Engineer.pdf (overwrites existing)
7. Re-run check.py on the generated PDF to verify
<!-- END MANAGED BUILD RULES -->

## Who this is
Vicky Kumar, Azure Data Engineer, 4+ years, TCS (GE HealthCare treasury).
Target: Senior Azure Data Engineer / Data Engineer, India (Bengaluru,
Hyderabad, Pune, Remote). Currently in Bhubaneswar, Odisha.

## Source of truth
profile/master.yaml. Nothing goes on a resume unless it is in that file.
If a fact is missing, ASK. Never estimate, never fill a gap with a guess.

## Pipeline - follow this order
1. python3 scripts/check.py <resume>        (see what the ATS reads)
2. python3 scripts/gap.py <resume> <jd>     (find real keyword gaps)
3. edit templates/resume.html               (one section at a time)
4. Chrome > Cmd+P > Save as PDF             (headers/footers OFF, scale 100%)
5. python3 scripts/check.py output/*.pdf    (prove it is fixed)

## Output files
- PDF from Chrome print  -> Greenhouse, Lever, Ashby, email, LinkedIn
- DOCX                   -> Workday and Taleo portals only
Both must carry identical facts.

## Format law
Single column. Headings exactly: Summary, Skills, Experience, Projects,
Certifications, Education. No tables. No text boxes. No icons or emoji.
No images. No colour. Nothing in a header or footer. Dates as "Mon YYYY".
One page.

## India - never put these on the resume
Photo, date of birth, marital status, father's or husband's name, full street
address, Aadhaar, caste, religion, passport number, expected CTC, a
"Declaration" block with a signature. They are useless to every parser and
hurt with MNCs, GCCs and global applications.

## Numbers
Vicky's real figures: 83% incident-time reduction, 99.9% SLA, 10+ pipelines,
15+ pipelines supported, 100+ failures resolved, 5 data sources, 1M+ records,
40% / 25% / 60% (round - these are his originals, do not change them, but
prefer real before/after numbers if he supplies them).
Never add a number he did not give.

## Style
Short answers. One task per reply. Show the command you ran and its real
output. Do not claim a score you did not measure.

## Target
Senior Azure Data Engineer / Data Engineer, India (PAN INDIA - open to
relocate anywhere in India, and Remote). Based in Bhubaneswar, Odisha. Focus on MNCs
(incl. their GCC/India arms): Microsoft, Amazon, Walmart Global Tech, Goldman
Sachs, Oracle, SAP, IBM, Accenture, Capgemini, Cognizant, Infosys, TCS, Deloitte.

## Research
All research uses live web tools (prefer parallel sub-agents + the parallel
MCP). Never answer market or job questions from memory. Never fabricate.