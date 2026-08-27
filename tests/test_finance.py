import pytest

from infrainvest.finance import irr, npv, payback_period, sensitivity_table


def test_npv():
    result = npv(0.10, [-1000, 600, 600])
    assert result == pytest.approx(41.32, abs=0.01)


def test_irr():
    result = irr([-1000, 600, 600])
    assert result == pytest.approx(0.13066, abs=1e-3)


def test_payback_period():
    assert payback_period([-1000, 400, 400, 400]) == 2.5


def test_sensitivity_table_size():
    scenarios = sensitivity_table(
        [-1000, 500, 600],
        discount_rates=[0.05, 0.10],
        revenue_multipliers=[0.9, 1.0, 1.1],
    )
    assert len(scenarios) == 6
