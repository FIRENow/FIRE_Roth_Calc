The Ret_Calc_Share.py program is my attempt to model a Roth conversion calculator. 

The program expects the user to update the following inputs per their personal scenario

  # Current age and expected remaining life span
  years = 55  
  ages = np.arange(45, 45 + years)
  
  # Financial assumptions
  initial_stock_balance = 2_000_000  
  initial_401k_balance = 750_000  
  initial_bonds_cash_balance = 250_000  
  initial_spending = 100_000  
  inflation_rate = 0.03  
  growth_rate = 0.07  
  capital_gains_rate = 0.15  
  ordinary_income_rate = 0.12  
  cost_basis_pct = 0.80  
  
  # Withdrawal logic
  cash_withdrawal_pct = 0.5  
  
  # Roth conversion assumptions
  roth_conversion_min = 60_000  
  roth_conversion_max = 70_000 

This program has been created after a ton of iterations with ChatGPT. It's not perfect, and requires the user to play around with the Roth conversion assumption numbers but gives a lot more control to see the impact of different Roth conversion strategies.

I have tested this on Python 3.9.4

Feedback welcome!
