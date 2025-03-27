import math

# input
selection = input("Calculate Call or Put?: ").strip().capitalize()
month = input("Enter the month of the " + selection + ": ")
curr_price = float(input("Enter the current price: "))
period_duration = float(input("Enter the period duration (in months): "))
period_times = int(input("Enter number of periods: "))
expected_up = float(input("Enter the growing percentage (as decimal, e.g. 0.06 for 6%): "))
expected_down = float(input("Enter the declining percentage (as decimal, e.g. -0.05 for -5%): "))
risk_free_rate = float(input("Enter the risk-free rate (as decimal per annum, e.g. 0.05 for 5%): "))
strike_price = float(input("Enter the strike price: "))

# 參數設定
u = 1 + expected_up
d = 1 - expected_down
dt = period_duration / 12  # 每期時間（年）
r = risk_free_rate

# risk-neutral probability
p = (math.exp(r * dt) - d) / (u - d)

# Step 1: 算終點價格
prices = [curr_price * (u ** j) * (d ** (period_times - j)) for j in range(period_times + 1)]

# Step 2: 建立final payoff
if selection == "Call":
    values = [max(price - strike_price, 0) for price in prices]
elif selection == "Put":
    values = [max(strike_price - price, 0) for price in prices]
else:
    raise ValueError("Invalid option type.")

# Step 3: 回推價格（discount 每期）
for i in range(period_times - 1, -1, -1):
    values = [
        math.exp(-r * dt) * (p * values[j + 1] + (1 - p) * values[j])
        for j in range(i + 1)
    ]

print(f"The {selection} price is: {values[0]:.4f}")
