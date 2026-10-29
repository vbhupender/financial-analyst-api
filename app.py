# 1. Defining different data types
company_name = "AlphaCorp"           # String
token_count = 1450                  # Integer
latency_seconds = 2.45              # Float
is_inference_successful = True      # Boolean

# 2. Printing the values and their "Types"
print("--- Checking Data Types ---")
print(f"Company: {company_name} | Type: {type(company_name)}")
print(f"Tokens: {token_count} | Type: {type(token_count)}")
print(f"Latency: {latency_seconds}s | Type: {type(latency_seconds)}")
print(f"Success: {is_inference_successful} | Type: {type(is_inference_successful)}")

# 3. The Danger Zone: Unintentional mixing
print("\n--- Simulating an Error ---")
revenue_text = "500000"  # This looks like a number, but it's wrapped in quotes (a String!)
expenses = 350000        # This is a real Integer

clear_revenue = int(revenue_text)
# Un-comment the line below to see what happens when you mix types!
total_profit = clear_revenue - expenses
print(f'Fixed total profit: ${total_profit}')