# -*- coding: utf-8 -*-
"""
GenPark Accio C-Suite Manager Client
Zero-dependency corporate OKR strategic alignment DAG solver, capital expenditure hurdle IRR/NPV evaluator,
and board executive briefing synthesis matrix engine.
"""

import math
from typing import Dict, List, Any, Optional

class GenParkAccioCSuiteManager:
    """
    Aligns enterprise OKR hierarchies, evaluates CapEx investment hurdles (NPV/IRR),
    and synthesizes C-suite board briefs.
    """

    def resolve_okr_alignment_dag(
        self,
        objectives: List[Dict[str, Any]],
        key_results: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Evaluates hierarchical OKR alignment DAG: Company Objectives -> Team Objectives -> Key Results.
        """
        if not objectives:
            raise ValueError("Objectives list cannot be empty.")

        # Map KRs to objectives
        kr_by_obj = {}
        for kr in key_results:
            parent_id = kr.get("objective_id", "")
            kr_by_obj.setdefault(parent_id, []).append(kr)

        scored_objectives = []
        overall_progress_sum = 0.0

        for obj in objectives:
            obj_id = obj.get("id", "")
            krs = kr_by_obj.get(obj_id, [])

            if krs:
                total_w = sum(kr.get("weight", 1.0) for kr in krs)
                progress = sum(kr.get("progress_pct", 0.0) * kr.get("weight", 1.0) for kr in krs) / max(1e-9, total_w)
            else:
                progress = obj.get("self_reported_progress_pct", 0.0)

            progress_val = round(progress, 1)
            overall_progress_sum += progress_val

            status = "ON_TRACK" if progress_val >= 70.0 else ("AT_RISK" if progress_val >= 40.0 else "OFF_TRACK")

            scored_objectives.append({
                "objective_id": obj_id,
                "title": obj.get("title", "Corporate Goal"),
                "tier": obj.get("tier", "company"),
                "linked_krs_count": len(krs),
                "weighted_progress_pct": progress_val,
                "status": status
            })

        avg_company_progress = round(overall_progress_sum / len(objectives), 1)

        return {
            "total_objectives": len(objectives),
            "total_key_results": len(key_results),
            "enterprise_okr_progress_pct": avg_company_progress,
            "company_health": "STRONG_EXECUTION" if avg_company_progress >= 70.0 else ("MODERATE_DELAYS" if avg_company_progress >= 50.0 else "STRATEGIC_ALIGNMENT_ALERT"),
            "evaluated_objectives": scored_objectives
        }

    def calculate_capex_npv_and_irr(
        self,
        initial_investment_usd: float,
        cash_flows_usd: List[float],
        hurdle_discount_rate: float = 0.12
    ) -> Dict[str, Any]:
        """
        Calculates Net Present Value (NPV) and Internal Rate of Return (IRR) using bisection solver.
        """
        if initial_investment_usd <= 0 or not cash_flows_usd:
            raise ValueError("Investment must be positive and cash flows list non-empty.")

        # NPV formula: -I0 + sum(CF_t / (1 + r)^t)
        def calc_npv(rate: float) -> float:
            val = -initial_investment_usd
            for t, cf in enumerate(cash_flows_usd, start=1):
                val += cf / math.pow(1.0 + rate, t)
            return val

        project_npv = round(calc_npv(hurdle_discount_rate), 2)

        # Solve for IRR: rate where calc_npv(rate) == 0 via bisection
        low_r = -0.5
        high_r = 2.0
        irr = None

        for _ in range(60):
            mid_r = (low_r + high_r) / 2.0
            npv_mid = calc_npv(mid_r)
            if abs(npv_mid) < 1.0:
                irr = mid_r
                break
            if npv_mid > 0:
                low_r = mid_r
            else:
                high_r = mid_r

        irr_pct = round(irr * 100.0, 2) if irr is not None else None

        # Investment Decision
        is_viable = project_npv > 0 and (irr is not None and irr >= hurdle_discount_rate)

        # Payback period (undiscounted)
        cum_cf = 0.0
        payback_period_years = None
        for t, cf in enumerate(cash_flows_usd, start=1):
            cum_cf += cf
            if cum_cf >= initial_investment_usd and payback_period_years is None:
                payback_period_years = t

        return {
            "initial_investment_usd": initial_investment_usd,
            "hurdle_discount_rate_pct": round(hurdle_discount_rate * 100.0, 1),
            "net_present_value_usd": project_npv,
            "internal_rate_of_return_pct": irr_pct,
            "simple_payback_period_years": payback_period_years,
            "investment_verdict": "APPROVE_CAPEX" if is_viable else "REJECT_CAPEX",
            "decision_rationale": "IRR exceeds corporate hurdle rate and NPV is positive." if is_viable else "Investment does not meet corporate return thresholds."
        }

    def synthesize_executive_brief_matrix(
        self,
        kpis: Dict[str, Any],
        strategic_initiatives: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Synthesizes high-level board summary matrix across Revenue, Burn Rate, Runway, and Strategy.
        """
        arr = kpis.get("arr_usd", 1000000.0)
        burn = kpis.get("monthly_net_burn_usd", 50000.0)
        cash = kpis.get("cash_balance_usd", 1200000.0)
        runway_months = round(cash / max(1.0, burn), 1)

        # Strategy progress
        total_initiatives = len(strategic_initiatives)
        completed = sum(1 for init in strategic_initiatives if init.get("progress_pct", 0) >= 100)
        avg_progress = sum(init.get("progress_pct", 0) for init in strategic_initiatives) / max(1, total_initiatives)

        # Composite governance score (0-100)
        runway_score = min(40.0, runway_months * 2.0)
        progress_score = avg_progress * 0.4
        arr_growth_score = min(20.0, kpis.get("arr_growth_rate_pct", 50.0) * 0.3)
        governance_health = round(runway_score + progress_score + arr_growth_score, 1)

        return {
            "key_metrics": {
                "arr_usd": arr,
                "cash_runway_months": runway_months,
                "monthly_burn_usd": burn,
                "net_burn_multiple": round(burn * 12.0 / max(1.0, arr), 2)
            },
            "strategic_execution": {
                "total_initiatives": total_initiatives,
                "completed_count": completed,
                "average_progress_pct": round(avg_progress, 1)
            },
            "governance_health_score": governance_health,
            "executive_brief_status": "EXCELLENT_TRAJECTORY" if governance_health >= 75.0 else ("STABLE_WATCH" if governance_health >= 50.0 else "URGENT_INTERVENTION_REQUIRED")
        }
