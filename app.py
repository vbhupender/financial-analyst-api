
quarterly_revenues = [120000, 150000, 135000, 180000]

print(f'Q1 Revenue: ${quarterly_revenues[0]}')

company_profile = {
    "name" : "Alpha Corp",
    "ticker": "ALPH",
    "is_profitable": True,
    "annual_total": sum(quarterly_revenues)
}

print("\n ---Company Profile Dictionay---")
print(f'Compnay Name: {company_profile["name"]}')
print(f'Ticker Symbol:{company_profile["ticker"]}')
print(f'Calculated Annual Revenue: ${company_profile["annual_total"]}')

company_profile["risk_level"] = "low"
print(f'Updated Company Profile:{company_profile}')
