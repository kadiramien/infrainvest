# InfraInvest

A Python toolkit for evaluating infrastructure projects using discounted cash flow, IRR, payback and scenario sensitivity analysis.

The project sits at the intersection of **engineering economics, finance and software**: turn project cash-flow assumptions into reproducible investment metrics instead of relying on opaque spreadsheet calculations.

## What it does

- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Simple payback period
- Discount-rate sensitivity
- Revenue/upside/downside scenarios
- Reproducible Python calculations with automated tests

## Example

```python
from infrainvest import irr, npv, payback_period

cash_flows = [
    -10_000_000,
    1_800_000,
    2_100_000,
    2_400_000,
    2_700_000,
    3_000_000,
]

print(npv(0.08, cash_flows))
print(irr(cash_flows))
print(payback_period(cash_flows))
```

## Why infrastructure?

Infrastructure decisions combine technical constraints with capital allocation. A project can be operationally attractive but financially weak once financing assumptions, discount rates and downside cases are considered.

InfraInvest makes those assumptions explicit and testable.

## Project structure

```text
infrainvest/
  finance.py        # NPV, IRR, payback and sensitivity engine
tests/
  test_finance.py   # automated tests
example.py          # worked project appraisal
```

## Run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python example.py
```

## Engineering choices

- Core calculations are implemented as pure functions to keep them easy to test and reuse.
- No spreadsheet state or hidden formulas: inputs and outputs are explicit.
- CI runs the test suite on every push and pull request.

## Roadmap

- Monte Carlo modelling for construction cost and demand uncertainty
- debt-service coverage and financing structure
- inflation/indexation scenarios
- portfolio comparison and ranking
- lightweight web/API interface

## Author

Amien Kadir — Mechanical Engineering student building software at the intersection of engineering, finance and data.
