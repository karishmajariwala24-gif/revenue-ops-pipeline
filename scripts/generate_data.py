"""
Project 7 — Generate Sample Deal Data
Creates realistic B2B sales pipeline data for:
- Asana workflow import
- Power BI dashboard

30 deals across 4 stages, 3 reps, 5 industries
Includes billing reconciliation status
"""

import pandas as pd
import random
from datetime import datetime, timedelta
import os

OUT_DIR = r"I:\My Drive\personal\Portfolio Projects\Project7-Revenue-Ops-Asana-PowerBI\data"
os.makedirs(OUT_DIR, exist_ok=True)

random.seed(42)

# ── REFERENCE DATA ────────────────────────────────────────────────────────────
COMPANIES = [
    ("Apex Cybersecurity", "Technology", "Enterprise"),
    ("Cascade Health Systems", "Healthcare", "Mid-Market"),
    ("Northstar Financial", "Finance", "Enterprise"),
    ("Greenleaf Organics", "Consumer Goods", "SMB"),
    ("Velocity Logistics", "Logistics", "Mid-Market"),
    ("Pinnacle Education Group", "Education", "Enterprise"),
    ("Redwood Manufacturing", "Manufacturing", "Mid-Market"),
    ("Summit Media Group", "Media", "SMB"),
    ("Ironclad Insurance", "Finance", "Enterprise"),
    ("Pacific Retail Corp", "Retail", "Mid-Market"),
    ("BlueShift Analytics", "Technology", "SMB"),
    ("Horizon Aerospace", "Aerospace", "Enterprise"),
    ("Metro Healthcare Partners", "Healthcare", "Mid-Market"),
    ("Ember Energy Solutions", "Energy", "Enterprise"),
    ("Coastal Real Estate Group", "Real Estate", "SMB"),
    ("Atlas Construction", "Construction", "Mid-Market"),
    ("Prism Software Inc", "Technology", "SMB"),
    ("Silver Creek Hotels", "Hospitality", "Mid-Market"),
    ("Falcon Defense Systems", "Aerospace", "Enterprise"),
    ("Riverdale Pharma", "Healthcare", "Enterprise"),
    ("Quantum Data Labs", "Technology", "SMB"),
    ("Oakwood Financial", "Finance", "Mid-Market"),
    ("Trident Shipping", "Logistics", "Enterprise"),
    ("Bloom Wellness", "Healthcare", "SMB"),
    ("Digital First Media", "Media", "SMB"),
    ("ClearView Optics", "Manufacturing", "Mid-Market"),
    ("Pioneer Education", "Education", "SMB"),
    ("SkyBridge Telecom", "Telecom", "Enterprise"),
    ("FreshStart Foods", "Consumer Goods", "Mid-Market"),
    ("CoreTech Solutions", "Technology", "Enterprise"),
]

REPS = ["Sarah Mitchell", "James Chen", "Priya Patel"]
STAGES = ["Lead", "Qualified", "Proposal", "Closed Won", "Closed Lost"]
LEAD_SOURCES = ["Inbound - Website", "Outbound - Cold Call", "Referral", "Event", "LinkedIn"]

STAGE_WEIGHTS = {
    "Lead": 0.15,
    "Qualified": 0.25,
    "Proposal": 0.20,
    "Closed Won": 0.25,
    "Closed Lost": 0.15,
}

BILLING_STATUS = ["Not Applicable", "Pending Reconciliation", "Reconciled", "Discrepancy Found", "Resolved"]

# ── GENERATE DEALS ────────────────────────────────────────────────────────────
deals = []
today = datetime(2026, 6, 15)

for i, (company, industry, segment) in enumerate(COMPANIES):
    # Assign rep round-robin
    rep = REPS[i % 3]

    # Deal value based on segment
    if segment == "Enterprise":
        deal_value = random.randint(50000, 250000)
    elif segment == "Mid-Market":
        deal_value = random.randint(15000, 75000)
    else:
        deal_value = random.randint(5000, 25000)

    # Stage
    stage = random.choices(list(STAGE_WEIGHTS.keys()), weights=list(STAGE_WEIGHTS.values()))[0]

    # Dates
    days_ago_created = random.randint(7, 120)
    created_date = today - timedelta(days=days_ago_created)

    # Stage progression dates
    qualified_date = created_date + timedelta(days=random.randint(3, 14)) if stage != "Lead" else None
    proposal_date  = qualified_date + timedelta(days=random.randint(5, 21)) if stage in ["Proposal","Closed Won","Closed Lost"] else None
    close_date     = proposal_date + timedelta(days=random.randint(7, 30)) if stage in ["Closed Won","Closed Lost"] else None

    # Expected close (for open deals)
    if stage in ["Lead","Qualified","Proposal"]:
        expected_close = today + timedelta(days=random.randint(14, 60))
    else:
        expected_close = close_date

    # Billing reconciliation (only for Closed Won)
    if stage == "Closed Won":
        billing = random.choices(
            ["Reconciled", "Pending Reconciliation", "Discrepancy Found", "Resolved"],
            weights=[0.5, 0.25, 0.15, 0.1]
        )[0]
        billing_amount = deal_value
        billed_amount  = deal_value if billing in ["Reconciled","Resolved"] else (
            deal_value - random.randint(500, 5000) if billing == "Discrepancy Found" else 0
        )
    else:
        billing = "Not Applicable"
        billing_amount = 0
        billed_amount  = 0

    # Days in current stage
    if stage == "Lead":
        days_in_stage = (today - created_date).days
    elif stage == "Qualified":
        days_in_stage = (today - qualified_date).days
    elif stage == "Proposal":
        days_in_stage = (today - proposal_date).days
    else:
        days_in_stage = 0

    # Follow-up status
    if stage in ["Lead", "Qualified", "Proposal"]:
        last_activity = today - timedelta(days=random.randint(0, 14))
        days_since_activity = (today - last_activity).days
        follow_up_status = "Overdue" if days_since_activity > 7 else ("Due Soon" if days_since_activity > 4 else "On Track")
    else:
        last_activity = close_date if close_date else today
        days_since_activity = 0
        follow_up_status = "Closed"

    # Lead source
    source = random.choice(LEAD_SOURCES)

    # Win probability
    prob_map = {"Lead": 10, "Qualified": 30, "Proposal": 60, "Closed Won": 100, "Closed Lost": 0}
    probability = prob_map[stage]

    deals.append({
        "deal_id"             : f"D{i+1:03d}",
        "company"             : company,
        "industry"            : industry,
        "segment"             : segment,
        "deal_value"          : deal_value,
        "stage"               : stage,
        "rep_owner"           : rep,
        "lead_source"         : source,
        "created_date"        : created_date.strftime("%Y-%m-%d"),
        "qualified_date"      : qualified_date.strftime("%Y-%m-%d") if qualified_date else "",
        "proposal_date"       : proposal_date.strftime("%Y-%m-%d") if proposal_date else "",
        "close_date"          : close_date.strftime("%Y-%m-%d") if close_date else "",
        "expected_close"      : expected_close.strftime("%Y-%m-%d") if expected_close else "",
        "days_in_stage"       : days_in_stage,
        "probability"         : probability,
        "weighted_value"      : int(deal_value * probability / 100),
        "last_activity"       : last_activity.strftime("%Y-%m-%d"),
        "days_since_activity" : days_since_activity,
        "follow_up_status"    : follow_up_status,
        "billing_status"      : billing,
        "billing_amount"      : billing_amount,
        "billed_amount"       : billed_amount,
        "billing_discrepancy" : billing_amount - billed_amount if billing == "Discrepancy Found" else 0,
        "notes"               : "",
    })

# ── SAVE ──────────────────────────────────────────────────────────────────────
df = pd.DataFrame(deals)

# Main dataset
df.to_csv(os.path.join(OUT_DIR, "pipeline_deals.csv"), index=False)
df.to_excel(os.path.join(OUT_DIR, "pipeline_deals.xlsx"), index=False)

# Asana import format (simplified for CSV import)
asana_df = df[["deal_id","company","industry","segment","deal_value","stage",
               "rep_owner","created_date","expected_close","follow_up_status",
               "billing_status"]].copy()
asana_df.columns = ["Task ID","Task Name","Industry","Segment","Deal Value","Section",
                    "Assignee","Start Date","Due Date","Priority","Status"]
asana_df["Task Name"] = df["company"] + " - $" + df["deal_value"].astype(str)
asana_df.to_csv(os.path.join(OUT_DIR, "asana_import.csv"), index=False)

# Power BI dataset (full detail)
df.to_csv(os.path.join(OUT_DIR, "powerbi_dataset.csv"), index=False)

# Summary stats
print("="*60)
print("PROJECT 7 — SAMPLE DATA GENERATED")
print("="*60)
print(f"\n  Total deals: {len(df)}")
print(f"\n  By Stage:")
print(df["stage"].value_counts().to_string())
print(f"\n  By Rep:")
print(df["rep_owner"].value_counts().to_string())
print(f"\n  By Industry:")
print(df["industry"].value_counts().to_string())
print(f"\n  Pipeline Summary:")
print(f"    Total pipeline value     : ${df['deal_value'].sum():,.0f}")
print(f"    Weighted pipeline        : ${df['weighted_value'].sum():,.0f}")
print(f"    Closed Won revenue       : ${df[df['stage']=='Closed Won']['deal_value'].sum():,.0f}")
print(f"    Avg deal size            : ${df['deal_value'].mean():,.0f}")
print(f"    Avg days in stage (open) : {df[df['stage'].isin(['Lead','Qualified','Proposal'])]['days_in_stage'].mean():.0f}")
print(f"\n  Billing Reconciliation:")
print(df["billing_status"].value_counts().to_string())
discrepancy = df[df["billing_status"] == "Discrepancy Found"]["billing_discrepancy"].sum()
print(f"    Total discrepancies      : ${discrepancy:,.0f}")
print(f"\n  Follow-up Status (open deals):")
open_deals = df[df["stage"].isin(["Lead","Qualified","Proposal"])]
print(open_deals["follow_up_status"].value_counts().to_string())
print(f"\n  Files saved to: {OUT_DIR}")
print(f"    pipeline_deals.csv     — full dataset")
print(f"    pipeline_deals.xlsx    — full dataset (Excel)")
print(f"    asana_import.csv       — simplified for Asana CSV import")
print(f"    powerbi_dataset.csv    — full detail for Power BI")
print("="*60)
