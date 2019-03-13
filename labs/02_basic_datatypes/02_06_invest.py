'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

from decimal import *
total = input("investment amount: ")
interest_rate = input("enter your interest rate %: ")
years = input ("number of years you'd like to invest your funds: ")

interest_rate = (float(interest_rate) / 100 ) + 1

total = int(total) * 100

i = 0

while i < int(years):
    total = int(total) * float(interest_rate)
    i+= 1


total = int(total)/100
print("at the end of your term you'll have $" , total , ".")

