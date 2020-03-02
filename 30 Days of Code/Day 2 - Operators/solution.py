#!/usr/local/bin/python3

"""Task 

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
Complete the stub code provided in your editor to print whether or not n is weird.
"""

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100)))

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
solve(meal_cost, tip_percent, tax_percent)
