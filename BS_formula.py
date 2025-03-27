import math

# 參數輸入
selection = input("Calculate Call or Put?: ").strip().capitalize()
stock_price = float(input("Enter the stock price: "))
dividend_yield = float(input("Enter the dividend yield: (in float) "))
risk_free_rate = float(input("Enter the risk free rate: (in float) "))
month = int(input("Enter the month of the " + selection + ": "))
strike_price = float(input("Enter the strike price: "))

S = stock_price
q = dividend_yield
T = month / 12
K = strike_price
r = risk_free_rate

if selection == "Call":
    p = float(input("Enter the put price: "))
    c = p + S * math.exp(-q * T) - K * math.exp(-r * T)
    print("The value of the call option is: " + str(c))

elif selection == "Put":
    c = float(input("Enter the call price: "))
    p = c + K * math.exp(-r * T) - S * math.exp(-q * T)
    print("The value of the put option is: " + str(p))

else:
    print("Invalid input")
