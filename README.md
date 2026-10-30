# genpark-accio-csuite-manager

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Accio C-Suite Manager is a zero-dependency executive decision-support and corporate governance engine implementing hierarchical OKR progress DAG alignment, capital expenditure financial hurdle rate analysis (Net Present Value NPV and Internal Rate of Return IRR), and board briefing synthesis matrices.

```mermaid
flowchart TD
    A[Company & Team OKRs] --> B[Hierarchical Progress DAG Evaluator]
    B --> C[Weighted Enterprise Alignment Score]
    D[Investment Cash Flows & Discount Rate] --> E[NPV & Bisection IRR Solver]
    E --> F[CapEx Hurdle Approval Decision]
    G[Financial KPIs & Strategic Goals] --> H[C-Suite Synthesis Matrix]
    H --> I[Runway, Burn Multiple & Board Brief]
```

## Features
- **Hierarchical OKR Alignment**: Maps department and team key results to high-level corporate strategic objectives with automated status propagation.
- **CapEx Financial Hurdle Solver**: Evaluates capital deployment using exact discounted cash flow (NPV) and iterative IRR root finding.
- **Executive Governance Brief**: Computes corporate burn multiple, cash runway, and strategic initiative health for board reporting.

## Quickstart

```python
from client import GenParkAccioCSuiteManager

csuite = GenParkAccioCSuiteManager()
res = csuite.calculate_capex_npv_and_irr(100000.0, [30000, 40000, 50000, 60000], 0.12)
print("NPV:", res["net_present_value_usd"], "IRR:", res["internal_rate_of_return_pct"])
```

## License
MIT
