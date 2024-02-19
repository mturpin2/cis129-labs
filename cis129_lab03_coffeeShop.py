# CIS129 Module 3 Lab
# Coffee Shop
# Author: Micah Turpin

# This program demonstrates some of the basics of python.

# This program simulates a coffee shop experience where the user is asked for their choice of items with the program
# printing out a receipt depending on the users choices.

print('How many coffees would you like?')
noOfCoffees = int(input())
print('How many muffins would you like?')
noOfMuffins = int(input())
print('How many bagels would you like?')
noOfBagels = int(input())
print('How many cookies would you like?')
noOfCookies = int(input())
# Above statements ask the user for input, specifically how many coffees, muffins, bagels and cookies they would like to order.

COFFEE_PRICE = 5
MUFFIN_PRICE = 4
BAGEL_PRICE = 4
COOKIE_PRICE = 3
TAX = 0.06
# Set constants for the prices of the items and tax value.

coffeeSubtotal = noOfCoffees * COFFEE_PRICE
muffinSubtotal = noOfMuffins * MUFFIN_PRICE
bagelSubtotal = noOfBagels * BAGEL_PRICE
cookieSubtotal = noOfCookies * COOKIE_PRICE
taxSubtotal = (coffeeSubtotal + muffinSubtotal + bagelSubtotal + cookieSubtotal) * TAX
grandTotal = coffeeSubtotal + muffinSubtotal + bagelSubtotal + cookieSubtotal + taxSubtotal
# Processes the users input along with programs constants, resulting in totals required for receipt.

print('\n' + 'Micah\'s Coffee Shop'.center(35,'*') + '\n')
print('Number of coffees bought:')
print(noOfCoffees)
print('Number of muffins bought:')
print(noOfMuffins)
print('Number of bagels bought:')
print(noOfBagels)
print('Number of cookies bought:')
print(noOfCookies)
print('\n' + 'Micah\'s Coffee Shop'.center(35,'*') + '\n')
# Begins display of receipt, printing total number of items bought with some formatting to enhance the output.
# For example using .center on strings to center them and fill in blank space with * characters.

print(str(noOfCoffees) + ' Coffees at $5 each: $' + str(coffeeSubtotal))
print(str(noOfMuffins) + ' Muffins at $4 each: $' + str(muffinSubtotal))
print(str(noOfBagels) + ' Bagels at $4 each: $' + str(bagelSubtotal))
print(str(noOfCookies) + ' Cookies at $3 each: $' + str(cookieSubtotal))
print('6% tax: $' + str(round(taxSubtotal, 2)))
print('----------' + '\nTotal: $' + str(round(grandTotal, 2)))
print('\n' + 'Micah\'s Coffee Shop'.center(35,'*'))
# Prints all of the totals.
# I was wondering how to get the program to not output more than 2 decimal places so I did some research and found
# the round function to further enhance the output of the program.

print('\n' + 'Thank you for coming!'.center(35))
print('Please come again'.center(35))
# Thanks the user for coming to the shop and to please come again. Uses .center to enhance output.
