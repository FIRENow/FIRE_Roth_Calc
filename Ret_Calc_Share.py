# Import necessary libraries and set up the environment for the simulation
import numpy as np
import pandas as pd

# Define variables for the simulation
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
cash_withdrawal_pct = 0.5  # No more than 50% of bonds/cash withdrawn in early years

# Roth conversion assumptions
roth_conversion_min = 60_000  # Minimum Roth conversion amount per year. 
roth_conversion_max = 70_000  # Maximum Roth conversion amount per year

# Initializing arrays to store balances, withdrawals, and taxes
stock_balances = np.zeros(years)
balances_401k = np.zeros(years)
bonds_cash_balances = np.zeros(years)
total_spending = np.zeros(years)
stock_withdrawals = np.zeros(years)
bonds_cash_withdrawals = np.zeros(years)
stock_gains = np.zeros(years)
AGI = np.zeros(years)
tax_due = np.zeros(years)
roth_conversions = np.zeros(years)
roth_balances = np.zeros(years)
tax_bracket = np.zeros(years)

# Initial balances
stock_balances[0] = initial_stock_balance
balances_401k[0] = initial_401k_balance
bonds_cash_balances[0] = initial_bonds_cash_balance

# Simulation loop
for i in range(years):
    if i > 0:
        # Increase spending and adjust for inflation
        total_spending[i] = total_spending[i-1] * (1 + inflation_rate)
    else:
        total_spending[i] = initial_spending
    
    # Conservative withdrawals from bonds/cash (no more than 50% in the first years)
    if bonds_cash_balances[i] >= total_spending[i] * cash_withdrawal_pct:
        bonds_cash_withdrawals[i] = total_spending[i] * cash_withdrawal_pct
        bonds_cash_balances[i] -= bonds_cash_withdrawals[i]
        stock_withdrawals[i] = total_spending[i] - bonds_cash_withdrawals[i]
        stock_gains[i] = stock_withdrawals[i] * (1 - cost_basis_pct)
        AGI[i] = stock_gains[i]
        tax_due[i] = AGI[i] * capital_gains_rate
    else:
        # When bonds/cash runs below 50%, withdraw the remaining amount and more from stocks
        bonds_cash_withdrawals[i] = bonds_cash_balances[i]
        bonds_cash_balances[i] = 0
        stock_withdrawals[i] = total_spending[i] - bonds_cash_withdrawals[i]
        stock_gains[i] = stock_withdrawals[i] * (1 - cost_basis_pct)
        AGI[i] = stock_gains[i]
        tax_due[i] = AGI[i] * capital_gains_rate
        stock_balances[i] -= stock_withdrawals[i]
    
    # Roth conversions between $60,000 and $70,000 annually
    if balances_401k[i] > 0:
        roth_conversions[i] = min(max(roth_conversion_min, roth_conversion_max), balances_401k[i])
        balances_401k[i] -= roth_conversions[i]
        roth_balances[i] += roth_conversions[i]
        AGI[i] += roth_conversions[i]
        tax_due[i] += roth_conversions[i] * ordinary_income_rate

    # Grow the remaining stock, 401k, and Roth balances (assuming 7% annual return for all)
    if i < years - 1:
        stock_balances[i+1] = stock_balances[i] * 1.07
        balances_401k[i+1] = balances_401k[i] * 1.07
        roth_balances[i+1] = roth_balances[i] * 1.07
        bonds_cash_balances[i+1] = bonds_cash_balances[i]  # No growth assumed on bonds/cash

    # Update tax bracket based on AGI
    if AGI[i] <= 94_300:
        ordinary_income_rate = 0.12
    elif AGI[i] <= 201_050:
        ordinary_income_rate = 0.22
    elif AGI[i] <= 383_900:
        ordinary_income_rate = 0.24
    else:
        ordinary_income_rate = 0.32
    tax_bracket[i] = ordinary_income_rate * 100  # Convert to percentage for display

# Prepare updated output with cash/bonds withdrawals included
output_with_bonds_cash_withdrawals = pd.DataFrame({
    'Age': ages,
    'Stock Balance': stock_balances,
    'Stock Withdrawals': stock_withdrawals,
    'Capital Gains': stock_gains,
    'Bonds/Cash Withdrawals': bonds_cash_withdrawals,
    'Bonds/Cash Balance': bonds_cash_balances,
    '401K Balance': balances_401k,
    'Roth Conversions': roth_conversions,
    'Roth Balance': roth_balances,
    'AGI': AGI,
    'Tax Due': tax_due,
    'Tax Bracket (%)': tax_bracket  # Show tax bracket as percentage
})

# Print the results
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.0f}'.format)
print(output_with_bonds_cash_withdrawals)
