'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = int(input("Enter your investment amount: $"))
interest = float(input("Enter your interest rate in percentage: "))
years = int(input("Enter the number of years to invest: "))

future_value = amount * (1+interest/100) ** years
print("$" + str(round(future_value, 2)))
