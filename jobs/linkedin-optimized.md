# LinkedIn Profile: Optimized (paste-ready)

Built from `profile/master.yaml` (source of truth) + `jobs/market-research.md`
(15 JDs, Jul-Aug 2026) + your exported `Profile Linkedin.pdf` (2026-08-24).
Research date: market-research.md last_updated 2026-08-17. Every fact below is in
master.yaml or your existing LinkedIn profile. Nothing invented; no reach promised.

## 1. Headline (220 char limit)

```
Azure Data Engineer | 4.5 Years | Azure Data Factory (ADF), Databricks, PySpark, ADLS Gen2, Delta Lake, Microsoft Fabric | DP-700 Certified | TCS @ GE HealthCare Treasury | Open to Pan India & Remote
```

Why: recruiter search weighs headline most. Skill order follows measured JD frequency
(Databricks 80%, ADF/Delta/SQL 60%, PySpark 47%, Fabric 33%). Broader titles from
research ("Senior Data Engineer", "Databricks Engineer") go into Open-to-Work job
titles as search aliases, not into the headline itself.

## 2. About (natural voice, ~1,900 chars; first 300 chars show before "see more")

```
I build data pipelines that financial systems depend on, not just run.

At TCS, on the GE HealthCare Treasury account, I design and own end-to-end ETL/ELT pipelines that move exchange rates, Bloomberg and ODP feeds through a Medallion Architecture into Gold-layer datasets consumed by downstream systems. Ten-plus production pipelines, 99.9% SLA, no ambiguity about what happens when something breaks at 2 AM.

What I work with day to day:

Azure Data Factory, Databricks, PySpark, ADLS Gen2, Delta Lake, Synapse, Microsoft Fabric, Python, SQL, Azure DevOps CI/CD, ServiceNow.

Three things I'm proud of:

Cut incident resolution from 3-4 hours to under 30 minutes by building structured monitoring, logging and alerting instead of firefighting.
Tuned Delta Lake partitioning, Z-ordering and SQL joins for a 40% query performance gain.
Replaced legacy manual file-transfer workflows with event-driven pipelines, which removed inter-team dependencies and cut failure rates.

Before this role I spent 18 months in ETL support for BFSI reporting: 15+ pipelines, 100+ failures root-caused via SQL and ServiceNow. That's where I learned why pipelines fail, which is why mine log well.

Currently doing an Executive MBA in Data Science at IIT Patna (2025-2027). DP-700 certified (Fabric Data Engineer Associate); working toward the Databricks Data Engineer Associate cert.

Open to Azure Data Engineer / Senior Data Engineer roles across India or remote. Reach me via LinkedIn (linkedin.com/in/ervicky95) or GitHub (github.com/ervicky95).
```

## 3. Experience (official entries; fix these two things)

**Azure Data Engineer, GE HealthCare Treasury**
Tata Consultancy Services · Full-time · Sep 2023 - Present · Bhubaneswar

Keep your existing bullets (verified against master.yaml), plus these edits:
- Keep the client visible: title reads "Azure Data Engineer" with "GE HealthCare Treasury" in the description line.
- Attach both GitHub repos as media links (see section 5).
- Add one line at top naming the client domain: treasury and trade finance data.

**ETL Support Engineer, BFSI**
Tata Consultancy Services · Full-time · Mar 2022 - Aug 2023 · Bhubaneswar

Keep existing bullets. All five check out against master.yaml (15+ pipelines,
100+ failures resolved, validation/reconciliation).

Education fixes:
- Delete the duplicate third entry ("Gandhi Engineering College - India,
  Computational Science"). Same college listed three ways reads as neglect.
- Keep: IIT Patna eMBA (Aug 2025 - Aug 2027) and GEC B.Tech CSE (2016-2020).

## 4. Skills (ordered; add all 50 eventually, these first)

Order matters: the top 3 show on your profile card and collect endorsements first.
1. Azure Data Factory
2. Azure Databricks
3. PySpark
4. SQL
5. Python
6. Azure Data Lake Storage Gen2 (ADLS Gen2)
7. Delta Lake
8. Microsoft Fabric
9. Azure Synapse Analytics
10. ETL & ELT
11. Medallion Architecture
12. Data Lakehouse
13. Spark SQL
14. Azure DevOps
15. CI/CD
16. Data Warehousing
17. Data Modeling
18. Performance Tuning
19. Apache Airflow
20. dbt
21. n8n
22. Git
23. ServiceNow
24. Schema Drift Handling
25. Data Quality Validation
26. SLA Management
27. RBAC (Role-Based Access Control)
28. Monitoring
29. Error Handling
30. Data Ingestion
31. Data Integration
32. Generative AI (tooling: Claude Code, OpenAI Codex)

Do NOT add: Snowflake, Terraform, Power BI, DAX, Kafka, Unity Catalog, Purview.
master.yaml marks them `have: false`; they appear in JDs but you cannot defend
them in screening yet.

## 5. Projects & Featured

Featured section (currently empty): pin both GitHub repos.
- Urban Transit Medallion Pipeline: 1M+ records through Bronze/Silver/Gold,
  PySpark + Delta Lake, 40% query performance gain.
  github.com/ervicky95/urban-transit-medallion-pipeline
- Automated ETL Pipeline with n8n & LLM Integration: REST/RSS ingestion,
  OpenAI/Gemini transformation, 60% manual-effort reduction.
  github.com/ervicky95/n8n-data-pipeline-job-automation

Add a Projects entry for each with those two bullets. This gives recruiters
proof beyond the TCS bullets without exposing client internals.

## 6. Certifications (clean up)

Keep:
1. Microsoft Certified: Fabric Data Engineer Associate (DP-700)
2. Big Data Engineering Bootcamp with GCP and Azure Cloud
3. Generative AI for Leaders & Business Professionals

Remove (off-target noise for data engineering searches):
- Child Protection Results-Based Management Resource Pack
- Google Digital Marketing Garage Certification

Add once passed: Databricks Certified Data Engineer Associate (in progress;
master.yaml says pursuing, do not list as done until you pass).

## 7. Target settings

| Setting | Value |
|---|---|
| Open to Work | Recruiters only (you are employed; green banner optional) |
| Job titles | Azure Data Engineer, Senior Data Engineer, Data Engineer, Databricks Engineer, Analytics Engineer |
| Locations | Bengaluru, Hyderabad, Pune, Chennai, Kolkata, Delhi NCR, Bhubaneswar + Remote |
| Start date | Within 1 month (matches Naukri notice period; confirm it's true) |
| Location on profile | Bhubaneswar, Odisha, India (consistent everywhere) |

## 8. Measurements

One test, run 7 days after updating:
Ask a contact with Recruiter Lite (or use your own if available) to run a
LinkedIn Recruiter search: title "Data Engineer" OR "Azure Data Engineer",
keywords "Databricks AND PySpark AND ADLS", location Bengaluru/Hyderabad/Pune,
years 4-7. Pass = your profile appears in the first page of results. Log the
rank weekly alongside the Naukri Resdex test in jobs/naukri-optimized.md.

Secondary signals to watch monthly (profile views, search appearances are in
your LinkedIn dashboard): baseline them the day you update, compare after 30 days.
No promised numbers; only what you measure.

## 9. Research findings used (cross-checked once)

- Headline skills ordered by market-research.md frequency table: Databricks 12/15,
  SQL/ADF/Delta 9/15, PySpark 7/15, Fabric 5/15, Synapse/ADLS/CI-CD 4/15.
- Title set mirrors target_titles plus research aliases ("Senior Azure Data
  Engineer" recommended primary band, 4-6 yrs).
- Excluded skills match gaps_to_close have:false exactly (Snowflake, Terraform,
  Power BI/DAX, Kafka, Great Expectations).
- P0 actions from research (Terraform, Power BI basics, Unity Catalog awareness)
  are learning items, not profile claims; revisit after master.yaml updates.
