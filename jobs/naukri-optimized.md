# Naukri Profile: Optimized (paste-ready)

Built from `profile/master.yaml` (source of truth) + `jobs/market-research.md`
(15 JDs, Jul-Aug 2026, India) + the current Naukri 360 Pro dump (2026-08-23).
Every fact below exists in master.yaml or your live Naukri profile. Nothing invented.

---

## 1. Resume Headline (the single most weighted Naukri field)

```
Azure Data Engineer | 4.5 Years | ADF, Azure Databricks, PySpark, ADLS Gen2, Delta Lake, Microsoft Fabric, Azure Synapse | DP-700 | GE HealthCare @ TCS
```

Why this order (from market-research.md skill frequency): Databricks 80% of JDs,
ADF/SQL/Delta 60%, PySpark 47%, Fabric 33%. Title mirrors target_titles[0] +
research-recommended "Senior Azure Data Engineer" band (4-6 yrs sweet spot).

## 2. Profile Summary (~2000 char limit; paste whole block)

```
Azure Data Engineer with 4.5 years at Tata Consultancy Services, currently building production ETL/ELT pipelines for GE HealthCare Treasury & Trade Finance. Core stack: Azure Data Factory (ADF), Azure Databricks, PySpark, Azure Data Lake Storage Gen2 (ADLS Gen2), Delta Lake, Azure Synapse Analytics and Microsoft Fabric, built on Medallion Architecture (Bronze/Silver/Gold) Data Lakehouse design. Built and own 10+ production pipelines ingesting Bloomberg, ODP and treasury feeds at a 99.9% Service Level Agreement (SLA); cut incident resolution time 83% via structured logging, alerting and a triage runbook. Strong in SQL, Python and Continuous Integration/Continuous Delivery (CI/CD) via Azure DevOps across dev, QA and prod; tuned Delta Lake partitioning and Z-ordering for 40% analytical performance gains. Previously resolved 100+ ETL failures in BFSI support using SQL root-cause analysis and ServiceNow. Microsoft Certified: Fabric Data Engineer Associate (DP-700); pursuing Databricks Certified Data Engineer Associate; Executive MBA (Data Science) at IIT Patna. Open to Azure Data Engineer / Senior Data Engineer / Databricks Engineer roles. Pan India (willing to relocate anywhere) or Remote.
```

First 200 chars carry: exact title, years, TCS, GE HealthCare client: what recruiters
see in list view before clicking.

## 3. Key Skills (exactly 20, all verified in master.yaml; order = market weight)

```
Azure Data Factory (ADF), Azure Databricks, PySpark, SQL, Python, Azure Data Lake Storage Gen2 (ADLS Gen2), Delta Lake, Microsoft Fabric, Azure Synapse Analytics, ETL/ELT, Medallion Architecture, Data Lakehouse, Spark SQL, Azure DevOps, CI/CD (Continuous Integration/Continuous Delivery), Data Warehousing, Data Modeling, Performance Tuning, SLA Management, ServiceNow
```

Deliberately excluded (master.yaml marks these `have: false`): Snowflake, Terraform,
Power BI/DAX, Kafka/Event Hubs, Great Expectations. Do not tag a skill you cannot
defend in a screening call.

## 4. Employment (two blocks)

**Azure Data Engineer, GE HealthCare Treasury & Trade Finance**
Tata Consultancy Services | India | Sep 2023 - Present
- Built and own 10+ ETL/ELT pipelines in ADF and Databricks landing Bloomberg, ODP and internal treasury feeds into ADLS Gen2 for 3 downstream systems.
- Cut incident resolution from 3-4 hours to 30 minutes (83%) via structured logging, alerting and a triage runbook; held 99.9% SLA with validation checkpoints and event-based triggers.
- Reusable PySpark modules for incremental load and schema drift cut new-source onboarding effort 25%; Delta Lake partitioning/Z-ordering tuning gave a 40% performance gain; Azure DevOps CI/CD across dev, QA, prod.

**ETL Support Engineer, BFSI**
Tata Consultancy Services | India | Mar 2022 - Aug 2023
- Monitored 15+ production ETL pipelines for BFSI reporting cycles, owning the overnight batch window.
- Resolved 100+ pipeline failures via SQL root-cause analysis and ServiceNow incident management; ran end-to-end data validation and reconciliation before each reporting cycle.

## 5. IT Skills grid (Naukri version/last-used/experience fields)

| Skill | Last used | Experience |
|---|---|---|
| Azure Data Factory | 2026 | 4 Yrs |
| Azure Databricks | 2026 | 4 Yrs |
| PySpark | 2026 | 4 Yrs |
| ADLS Gen2 | 2026 | 4 Yrs |
| SQL | 2026 | 4 Yrs |
| Python | 2026 | 4 Yrs |
| ETL | 2026 | 4 Yrs |
| Azure Synapse Analytics | 2026 | 3 Yrs |
| Microsoft Fabric | 2026 | 1 Yr |
| Delta Lake, Azure DevOps, CI/CD, ServiceNow | 2026 | add rows |

## 6. Projects (keep both; links already on profile)

**Urban Transit Medallion Pipeline** (Freelancer, Feb-Mar 2026): github.com/ervicky95/urban-transit-medallion-pipeline
- 1M+ records through Bronze/Silver/Gold with PySpark transforms and Delta Lake optimization; query performance up 40%.

**Automated ETL Pipeline with n8n & LLM Integration** (Freelancer, Jun 2025-Jan 2026): github.com/ervicky95/n8n-data-pipeline-job-automation
- REST API + RSS ingestion into structured datasets via n8n orchestration; OpenAI/Gemini LLM transformation; manual effort down 60%.

## 7. Certifications (order: differentiators first)

1. Microsoft Certified: Fabric Data Engineer Associate (DP-700), valid to Apr 2027 (already on profile)
2. Databricks Certified Data Engineer Associate, **Pursuing** (add it; currently missing)
3. Big Data Engineering Bootcamp (GCP & Azure Cloud), Udemy (already on profile)
4. Generative AI for Leaders (currently missing from Naukri; add it)

## 8. Education (fix the duplicate)

- Executive MBA, Data Science, IIT Patna (2025-2027, ongoing): **missing on Naukri, add it**
- B.Tech, Computer Science and Engineering, Gandhi Engineering College (GEC), Bhubaneswar (2016-2020)
- **Delete** the duplicate "GEC, BHUBANESWAR 2016-2020" entry.

## 9. Preferences (Career profile settings)

| Field | Set to |
|---|---|
| Preferred roles | Data Engineer, Azure Data Engineer, ETL Developer, Databricks Engineer |
| Job type | Permanent (+ Contractual if you mean it, otherwise untick) |
| Employment type | Full Time |
| Locations | Bengaluru, Hyderabad, Pune, Chennai, Kolkata, Delhi/NCR, Noida, Gurugram, Remote, Bhubaneswar |
| Expected CTC | ₹9,00,000 (kept; Naukri filters on it; never put it on the resume PDF) |
| Notice period | 1 Month (your profile says this; confirm it's true; master.yaml still has TODO) |

## 10. Five Alerts (fix these on Naukri today)

1. **Current CTC ₹4,50,000 is public.** Recruiters anchor on it against your ₹9L ask. If Naukri lets you restrict visibility (hide or show-to-selected), do it.
2. **Address says Bodh Gaya, Bihar** while headline/location say Bhubaneswar. Background-check teams flag mismatches. Set the current city consistently to Bhubaneswar.
3. **Duplicate education entry** (same degree listed twice). It reads as an unedited profile; delete one.
4. **Two certifications and the IIT Patna MBA are missing.** DP-700 alone isn't carrying the section; add all three (see sections 7-8).
5. **Date-gap answer needed:** B.Tech ended 2020, first role Mar 2022. Have a one-line answer ready, because recruiters check gaps first (open question in master.yaml).

## 11. One Test (measurable, run 7 days after updating)

Recruiter-search simulation: on Naukri Resdex (or ask a friend with recruiter access),
search "Azure Data Engineer" with keywords `Databricks PySpark ADLS`, experience 4-6 yrs,
locations Bengaluru + Hyderabad + Pune + Remote. Pass = profile appears in the top 50
results. Re-run weekly; log the result below.

## 12. Call-Quality Tracker (log every recruiter call here)

| Date | Company | Role asked | Source (search term they used) | CTC discussed | Next step |
|---|---|---|---|---|---|
| | | | | | |

Review rule: every Friday, count the calls. Fewer than 2 per week means the headline or
skills tags miss what recruiters search; re-run this doc against fresh JDs.

## 13. Research Findings Used (cross-checked once)

- Skill order in headline/skills follows measured JD frequency: Databricks 80%, SQL/ADF/Delta 60%, PySpark 47%, Fabric 33%, Synapse/ADLS 27% (market-research.md, 15 JDs).
- "4.5 Years" matches master.yaml total_experience_years: 4.4 rounded up per required headline format, defensible (Mar 2022 to Aug 2026).
- Fabric positioned high despite 1 yr hands-on: DP-700 done + Fabric appears in 5/15 JDs including TCS Mumbai's own req.
- Cross-check: no headline/skill/number above lacks a master.yaml or live-Naukri source; gaps_to_close items excluded from skills tags.
