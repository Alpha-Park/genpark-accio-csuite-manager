# -*- coding: utf-8 -*-
"""
GenPark Accio C-Suite Manager FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkAccioCSuiteManager

mcp = FastMCP("genpark-accio-csuite-manager")
manager = GenParkAccioCSuiteManager()

@mcp.tool()
def resolve_okr_alignment_dag(
    objectives_json: str,
    key_results_json: str
) -> str:
    """
    Evaluates hierarchical OKR alignment DAG.
    """
    obj = json.loads(objectives_json)
    kr = json.loads(key_results_json)
    res = manager.resolve_okr_alignment_dag(obj, kr)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_capex_npv_and_irr(
    initial_investment_usd: float,
    cash_flows_usd_json: str,
    hurdle_discount_rate: float = 0.12
) -> str:
    """
    Calculates Net Present Value (NPV) and Internal Rate of Return (IRR).
    """
    cfs = json.loads(cash_flows_usd_json)
    res = manager.calculate_capex_npv_and_irr(initial_investment_usd, cfs, hurdle_discount_rate)
    return json.dumps(res, indent=2)

@mcp.tool()
def synthesize_executive_brief_matrix(
    kpis_json: str,
    strategic_initiatives_json: str
) -> str:
    """
    Synthesizes high-level board summary matrix across Revenue, Burn Rate, and Runway.
    """
    kpis = json.loads(kpis_json)
    inits = json.loads(strategic_initiatives_json)
    res = manager.synthesize_executive_brief_matrix(kpis, inits)
    return json.dumps(res, indent=2)

def main():
    print("Testing C-Suite Manager:")
    print(calculate_capex_npv_and_irr(100000.0, "[30000, 40000, 50000, 60000]", 0.10))

if __name__ == "__main__":
    main()
