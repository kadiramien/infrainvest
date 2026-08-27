from infrainvest import irr, npv, payback_period, sensitivity_table

cash_flows = [-10_000_000, 1_800_000, 2_100_000, 2_400_000, 2_700_000, 3_000_000]

print("NPV @ 8%:", npv(0.08, cash_flows))
print("IRR:", round(irr(cash_flows) * 100, 2), "%")
print("Payback:", payback_period(cash_flows), "years")

for scenario in sensitivity_table(
    cash_flows,
    discount_rates=[0.06, 0.08, 0.10],
    revenue_multipliers=[0.9, 1.0, 1.1],
):
    print(scenario)
