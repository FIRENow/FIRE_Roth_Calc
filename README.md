The Ret_Calc_Share.py program is my attempt to model a Roth conversion calculator. 

The program expects the user to update the following inputs per their personal scenario

  **#Current age and expected remaining life span****
  years = 55  # 100-year lifespan, retiree is currently 45 years old
  ages = np.arange(45, 45 + years)
  
  # Financial assumptions
  initial_stock_balance = 2_000_000  # Starting with $2M in stocks
  initial_401k_balance = 750_000  # $750K in pretax 401K
  initial_bonds_cash_balance = 250_000  # $$250K in cash and bonds
  initial_spending = 100_000  # Spending $100,000 per year
  inflation_rate = 0.03  # 3% inflation
  growth_rate = 0.07  # 7% growth rate
  capital_gains_rate = 0.15  # 15% capital gains tax rate
  ordinary_income_rate = 0.12  # 12% income tax rate for Roth conversions
  cost_basis_pct = 0.80  # 80% cost basis for stock withdrawals
  
  # Withdrawal logic
  cash_withdrawal_pct = 0.5  # No more than 50% of bonds/cash withdrawn in early years till the Roth ladder is mature
  
  # Roth conversion assumptions
  roth_conversion_min = 60_000  # Minimum Roth conversion amount per year. 
  roth_conversion_max = 70_000  # Maximum Roth conversion amount per year

This program has been created after a ton of iterations with ChatGPT. It's not perfect, and requires the user to play around with the Roth conversion assumption numbers but gives a lot more control to see the impact of different Roth conversion strategies.

I have tested this on Python 3.9.4

Feedback welcome!
