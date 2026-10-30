# -*- coding: utf-8 -*-
import json
from client import GenParkAccioCSuiteManager

csuite = GenParkAccioCSuiteManager()

# 1. OKR Strategic Alignment DAG
objs = [
    {"id": "obj_1", "title": "Scale Global ARR to $10M", "tier": "company"},
    {"id": "obj_2", "title": "Achieve SOC2 Type II Certification", "tier": "operations"}
]
krs = [
    {"objective_id": "obj_1", "title": "Close 15 Enterprise Pilots", "progress_pct": 80.0, "weight": 2.0},
    {"objective_id": "obj_1", "title": "Expand Net Retention to 125%", "progress_pct": 65.0, "weight": 1.0},
    {"objective_id": "obj_2", "title": "Audit Internal Access Controls", "progress_pct": 95.0, "weight": 1.0}
]
okr_res = csuite.resolve_okr_alignment_dag(objs, krs)
print(f"Corporate OKR Progress: {okr_res['enterprise_okr_progress_pct']}% ({okr_res['company_health']})")
for o in okr_res["evaluated_objectives"]:
    print(f"  [{o['status']}] {o['title']}: {o['weighted_progress_pct']}% (KRs: {o['linked_krs_count']})")

# 2. CapEx NPV & IRR Hurdle Analysis
cash_flows = [35000.0, 45000.0, 55000.0, 65000.0]
capex = csuite.calculate_capex_npv_and_irr(initial_investment_usd=120000.0, cash_flows_usd=cash_flows, hurdle_discount_rate=0.12)
print()
print(f"CapEx Financial Evaluation: NPV=${capex['net_present_value_usd']} | IRR={capex['internal_rate_of_return_pct']}% (Hurdle: {capex['hurdle_discount_rate_pct']}%)")
print(f"  Decision: {capex['investment_verdict']} -> {capex['decision_rationale']}")

# 3. Executive Board Briefing Synthesis
kpis = {"arr_usd": 4500000.0, "monthly_net_burn_usd": 120000.0, "cash_balance_usd": 3600000.0, "arr_growth_rate_pct": 85.0}
inits = [
    {"name": "EU Region Expansion", "progress_pct": 80.0},
    {"name": "Autonomous Agent Marketplace", "progress_pct": 95.0}
]
brief = csuite.synthesize_executive_brief_matrix(kpis, inits)
print()
print(f"Executive Brief: Governance Score={brief['governance_health_score']}/100 ({brief['executive_brief_status']})")
print(f"  Runway: {brief['key_metrics']['cash_runway_months']} months | Burn Multiple: {brief['key_metrics']['net_burn_multiple']}x")
