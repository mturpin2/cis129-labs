# CIS129 Module 4 Lab
# Author: Micah Turpin
# 2/27/2024
# This program takes input from the user regarding their stores sales and sales increase data and then
# uses that data to determine what their store and employee bonuses shall be. Printing out these bonuses
# to the user.

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = 'Enter the monthly sales $'  # prompt will be a string literal

# This code gets the monthly sales
monthlySales = float(input(prompt))

# This code determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100

# This code determines the employee bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $" + str(storeAmount))
print("The employee bonus amount is $" + str(empAmount))
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')

