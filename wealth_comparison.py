import pandas as pd
import numpy as np

def calculate_real_estate(savings, property_price, rent, mortgage_rate=0.05, appreciation_rate=0.03, tax_rate=0.015, insurance_rate=0.005, maintenance_rate=0.01, years=30):
    if property_price:
        down_payment = max(0.05 * property_price, savings)  # Minimum 5% down payment or all savings
    else:
        down_payment = savings
        property_price = down_payment / 0.05

    loan_amount = property_price - down_payment
    monthly_mortgage_payment = (loan_amount * mortgage_rate / 12) / (1 - (1 + mortgage_rate / 12) ** (-years * 12))
   
    total_rent_savings = 0
    equity = down_payment
    property_value = property_price

    results = []
    for year in range(1, years + 1):
        property_value *= (1 + appreciation_rate)
        principal_paid = loan_amount * (year / years)  # Simplified approximation of principal paid
        equity = down_payment + principal_paid
        rent_savings = (rent - monthly_mortgage_payment) * 12
        total_rent_savings += max(rent_savings, 0)
        annual_expenses = property_value * (tax_rate + insurance_rate + maintenance_rate)
        net_value = equity + total_rent_savings - annual_expenses

        results.append({
            "Year": year,
            "Property Value": property_value,
            "Equity": equity,
            "Total Rent Savings": total_rent_savings,
            "Annual Expenses": annual_expenses,
            "Net Value": net_value
        })

    return pd.DataFrame(results)

def calculate_stock_market(savings, annual_return=0.07, dividend_yield=0.02, fees=0.01, years=30):
    portfolio_value = savings
    results = []

    for year in range(1, years + 1):
        dividend_income = portfolio_value * dividend_yield
        portfolio_growth = portfolio_value * (annual_return - fees)
        portfolio_value += dividend_income + portfolio_growth

        results.append({
            "Year": year,
            "Portfolio Value": portfolio_value,
            "Dividend Income": dividend_income,
            "Net Value": portfolio_value
        })

    return pd.DataFrame(results)

def display_comparison(real_estate_df, stock_market_df):
    comparison_df = pd.DataFrame({
        "Year": real_estate_df["Year"],
        "Real Estate Net Value": real_estate_df["Net Value"],
        "Stock Market Net Value": stock_market_df["Net Value"]
    })
    print(comparison_df)

# Example usage
savings = 30000
rent = 1500
property_price = 300000

real_estate_results = calculate_real_estate(savings=savings, property_price=property_price, rent=rent)
stock_market_results = calculate_stock_market(savings=savings)

display_comparison(real_estate_results, stock_market_results)