> Notes: https://hackmd.io/@OcYEG2gIQFidYwnciTRuew/SkEFBpKi1l
## 1. European Option Pricing - Binomial Tree Method
This is a Python script that calculates the **European Call or Put option price** using the **Binomial Tree Method**, based on user input.

這是一個透過 **二元樹法（Binomial Tree）** 計算 **歐式選擇權價格（買權或賣權）** 的 Python 程式

---
### Features 功能特色
- Supports both **Call** and **Put** options
- Flexible input: periods, up/down %, interest rate, etc.
- Supports continuous compounding
- Clear structure with backtracking valuation
- 適合學習「風險中性機率」與「折現回推法」
---
### User Input 使用者輸入

執行程式後，依序輸入以下資訊：
```
Calculate Call or Put?: Call 
Enter the month of the Call: 6 
Enter the current price: 50 
Enter the period duration (in months): 3
Enter number of periods: 2 
Enter the growing percentage (as decimal, e.g. 0.06 for 6%): 0.06 
Enter the declining percentage (as decimal, e.g. -0.05 for -5%): 0.05 
Enter the risk-free rate (as decimal per annum, e.g. 0.05 for 5%): 0.05 
Enter the strike price: 51
```
---

### 📊 Output 範例輸出

The Call price is: 1.6350

---

### How it works 程式邏輯

1. 根據輸入的成長/下跌比率建立終點資產價格。
2. 用歐式選擇權 payoff 計算到期價值。
3. 利用 **風險中性機率 + 折現回推法**，從到期日一層一層回推至現值。

---

### Example: Textbook Problem(From Options, Futures, and Other Derivatives, by J. C. Hull, 11th ed.)

Current price: 50 u = 1.06, d = 0.95 K = 51 r = 0.05 T = 6 months = 2 periods (3 months each)

✅ Correct result (matching textbook): `Call price ≈ 1.635`

---

### 🧑‍💻 Author

Written by [zackc0302]  

---

### 📂 File Info

- `Binomial_tree.py`：主程式，可直接執行
- **衍生性金融商品理論**使用
------
## 2. Put-Call Parity Calculator 📘📈

This Python script calculates the price of a **Call** or **Put** option using the **Put-Call Parity formula**, based on user input.

本程式透過 **買賣權平價關係（Put-Call Parity）** 計算未知的選擇權價格，支援 **考慮股利殖利率 (dividend yield)**，適合用於期權課程、金融衍生品作業或個人練習。

---

### Put-Call Parity Formula

For European options on dividend-paying stocks:

- **Call Price**: $C = P + S * e^{-qT} - K * e^{-rT}$
- **Put Price**:  $P = C + K * e^{-rT} - S * e^{-qT}$

Where:
- `S` = stock price
- `K` = strike price
- `T` = time to maturity (in years)
- `r` = risk-free interest rate (annualized, continuous compounding)
- `q` = dividend yield (annualized)
- `C`, `P` = call / put option price

---

### Features

- Choose whether to compute **Call** or **Put**
- Supports continuous compounding interest
- Supports dividend yield
- Step-by-step input for clarity

---
### 🧑‍💻 Author

Written by [zackc0302]  

---

### 📂 File Info

- `BS_formula.py`：主程式，可直接執行
- **衍生性金融商品理論**使用

