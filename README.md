# Revenue Operations — Campaign Pipeline System

## Overview
End-to-end revenue operations system demonstrating how a Sales Ops professional manages both daily workflow execution AND leadership reporting visibility.

**Two tools, two audiences:**
- **Asana** → operational layer (the team uses this daily)
- **Power BI** → reporting layer (leadership uses this for decisions)

---

## What This Project Does

### Asana — Operational Workflow
- Manages 30 B2B deals across 5 pipeline stages: Lead → Qualified → Proposal → Closed Won → Finance/Billing
- 6 custom fields tracking deal value, industry, segment, billing status, follow-up status, and rep owner
- 3 automation rules:
  - Deal moves to Closed Won → auto-creates "Finance: Billing Reconciliation" subtask
  - Due date approaching → flags follow-up status as "Due Soon"
  - Billing Status set to "Reconciled" → auto-marks task complete

### Power BI — Leadership Dashboard (3 Pages)

**Page 1 — Pipeline Overview**
- Total pipeline value ($2.67M) | Closed won revenue ($671K) | Total deals (30) | Avg deal size ($89K)
- Pipeline by stage (bar chart)
- Deals by industry (donut chart)
- Deals by rep (column chart)

**Page 2 — Revenue Performance**
- Revenue trend by month (line chart)
- Revenue by rep broken down by stage (stacked bar)
- Revenue by industry (treemap)
- Win rate KPI (23%)

**Page 3 — Operations Health**
- Billing reconciliation status (donut — reconciled vs pending vs discrepancy)
- Follow-up compliance (overdue vs on track)
- Average days in stage by rep (bar chart)
- Total billing discrepancy KPI ($3,613)
- Overdue deals table (filtered view of deals needing immediate attention)

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| Asana | Project/workflow management, automation rules, custom fields |
| Power BI Desktop | Data visualization, DAX measures, interactive dashboards |
| Python | Sample data generation (30 realistic B2B deals) |
| AI-Assisted Development | Built with Kiro AI for data generation and project setup |

---

## Pipeline Summary
| Metric | Value |
|--------|-------|
| Total Pipeline | $2,669,915 |
| Weighted Pipeline | $1,134,242 |
| Closed Won Revenue | $670,878 |
| Average Deal Size | $88,997 |
| Win Rate | 23% |
| Total Discrepancies | $3,613 |
| Overdue Follow-ups | 12 deals |
| Industries Covered | 14 |
| Sales Reps | 3 |

---

## Data Model
30 deals across:
- **5 stages:** Lead (6), Qualified (9), Proposal (6), Closed Won (7), Closed Lost (2)
- **3 reps:** Sarah Mitchell, James Chen, Priya Patel
- **14 industries:** Technology, Healthcare, Finance, Aerospace, Consumer Goods, etc.
- **3 segments:** Enterprise, Mid-Market, SMB

---

## Files
```
Project7-Revenue-Ops-Asana-PowerBI/
├── README.md
├── data/
│   ├── pipeline_deals.csv          # Full dataset (30 deals, 24 columns)
│   ├── pipeline_deals.xlsx         # Same data in Excel format
│   ├── asana_import.csv            # Simplified format for Asana CSV import
│   └── powerbi_dataset.csv         # Full detail for Power BI import
├── power_bi/
│   └── Revenue_Operations_Dashboard.pbix  # Power BI dashboard file
├── docs/
│   └── screenshots/                # Dashboard screenshots (add after building)
└── scripts/
    └── generate_data.py            # Python script that generated the sample data
```

---

## How to Reproduce

### Asana Setup
1. Create new project → Board view → 5 sections (Lead, Qualified, Proposal, Closed Won, Finance/Billing)
2. Add 6 custom fields (Deal Value, Industry, Segment, Billing Status, Follow-up Status, Rep Owner)
3. Import `asana_import.csv` via project menu → Import → CSV
4. Add 3 automation rules (see above)

### Power BI Setup
1. Open Power BI Desktop (free)
2. Get Data → CSV → load `powerbi_dataset.csv`
3. Build 3 dashboard pages with visualizations described above
4. Create DAX measures: Total Deals, Avg Deal Size, Win Rate, Total Discrepancy

---

## Skills Demonstrated
- Sales operations workflow design
- Cross-functional process coordination (Sales → Finance → Billing)
- Pipeline management and hygiene
- Dashboard design for executive visibility
- Data analysis and KPI reporting
- Process automation (Asana rules)
- DAX measures in Power BI
- Financial reconciliation tracking

---

## Author
**Karishma Jariwala**
- LinkedIn: [karishma-jariwala-1b15b233](https://linkedin.com/in/karishma-jariwala-1b15b233)
- GitHub: [karishmajariwala24-gif](https://github.com/karishmajariwala24-gif)

Built with AI-assisted development using Kiro AI.
