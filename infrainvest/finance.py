from __future__ import annotations


def npv(discount_rate: float, cash_flows: list[float]) -> float:
    """Return net present value where cash_flows[0] occurs at t=0."""
    if discount_rate <= -1:
        raise ValueError("discount_rate must be greater than -1")
    return round(
        sum(cf / ((1 + discount_rate) ** period) for period, cf in enumerate(cash_flows)),
        2,
    )


def irr(
    cash_flows: list[float],
    lower: float = -0.99,
    upper: float = 10.0,
    tolerance: float = 1e-7,
    max_iterations: int = 500,
) -> float:
    """Estimate IRR with bisection. Cash flows must contain both signs."""
    if not cash_flows or not any(cf < 0 for cf in cash_flows) or not any(cf > 0 for cf in cash_flows):
        raise ValueError("cash_flows must contain at least one positive and one negative value")

    low_value = npv(lower, cash_flows)
    high_value = npv(upper, cash_flows)
    if low_value * high_value > 0:
        raise ValueError("IRR is not bracketed in the configured search interval")

    for _ in range(max_iterations):
        midpoint = (lower + upper) / 2
        value = npv(midpoint, cash_flows)
        if abs(value) < tolerance:
            return midpoint
        if low_value * value <= 0:
            upper = midpoint
            high_value = value
        else:
            lower = midpoint
            low_value = value

    return (lower + upper) / 2


def payback_period(cash_flows: list[float]) -> float | None:
    """Return simple payback period in years, interpolating within the crossing year."""
    if not cash_flows:
        return None

    cumulative = cash_flows[0]
    if cumulative >= 0:
        return 0.0

    for year in range(1, len(cash_flows)):
        previous = cumulative
        cumulative += cash_flows[year]
        if cumulative >= 0:
            inflow = cash_flows[year]
            if inflow <= 0:
                return float(year)
            fraction = abs(previous) / inflow
            return round((year - 1) + fraction, 2)
    return None


def sensitivity_table(
    base_cash_flows: list[float],
    discount_rates: list[float],
    revenue_multipliers: list[float],
) -> list[dict]:
    """Generate NPV scenarios by scaling positive operating cash flows."""
    scenarios: list[dict] = []
    for rate in discount_rates:
        for multiplier in revenue_multipliers:
            adjusted = [
                base_cash_flows[0],
                *[
                    cf * multiplier if cf > 0 else cf
                    for cf in base_cash_flows[1:]
                ],
            ]
            scenarios.append(
                {
                    "discount_rate": rate,
                    "revenue_multiplier": multiplier,
                    "npv": npv(rate, adjusted),
                }
            )
    return scenarios
