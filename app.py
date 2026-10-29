
def calculate_financial_health(revenue, expenses):
    print("Processing Financial Data...")
    profit = revenue - expenses
    if profit > 0:
        status = "Healthy"
    else:
        status = "At Risk"
    return f"Status : {status} | Net Profit ${profit}"

company_name = "AlphaCorp"
company_revenue = 500000
company_expenses = 600000

report = calculate_financial_health(company_revenue, company_expenses)
print(f"--- Financial Report for {company_name}---")
print(report)
