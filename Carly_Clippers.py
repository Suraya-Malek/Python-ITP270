#!/bin/python3
# List of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "moh"]
# Prices of haircuts
prices = [30, 25, 40, 20, 20, 35, 50]
# Number of haircuts purchased last week
last_week = [2, 3, 5, 8, 4, 4, 2]
# 1. Calculate the average price of a haircut
total_price = 0
for price in prices:
    total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)
 # 2. Reduce all prices by $5
new_prices = [price - 5 for price in prices]
print("The new prices are: ", new_prices)
# Task 7-10: Calculate total revenue and average daily revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue is: " , total_revenue)
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue is: {average_daily_revenue}")
# Task 12-13: Find haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts under 30.00 dollars are: " , cuts_under_30)
