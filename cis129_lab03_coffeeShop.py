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
# Above two statements ask the user for input, specifically how many muffins and coffees they would like to order.

COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TAX = 0.06
# Set constants for the prices of the items and tax value.

coffeeSubtotal = noOfCoffees * COFFEE_PRICE
muffinSubtotal = noOfMuffins * MUFFIN_PRICE
taxSubtotal = (coffeeSubtotal + muffinSubtotal) * TAX
grandTotal = coffeeSubtotal + muffinSubtotal + taxSubtotal
# Processes the users input along with programs constants, resulting in totals required for receipt.

print()
print('\n' + 'Micah\'s Coffee Shop'.center(35,'*') + '\n')
print('Number of coffees bought:')
print(noOfCoffees)
print('Number of muffins bought:')
print(noOfMuffins)
print('\n' + 'Micah\'s Coffee Shop'.center(35,'*') + '\n')
# For example using .center on strings to center them and fill in blank space with * characters.
# Begins display of receipt, printing total number of items bought with some formatting to enhance the output.

print(str(noOfCoffees) + ' Coffees at $5 each: $' + str(coffeeSubtotal))
print(str(noOfMuffins) + ' Muffins at $4 each: $' + str(muffinSubtotal))
print('6% tax: $' + str(round(taxSubtotal, 2)))
print('----------' + '\nTotal: $' + str(round(grandTotal, 2)))
print('\n' + 'Micah\'s Coffee Shop'.center(35,'*'))
# Prints all of the totals.
# I was wondering how to get the program to not output more than 2 decimal places so I did some research and found
# the round function to further enhance the output of the program.
