# CIS129 Module 5 Lab
# Author: Micah Turpin
# 3/14/2024
# This program asks the user for the amount of bottles they have collected each day over the course
# of a week to calculate the total for the week and the subsequent payout for those bottles.
# It loops this function for as many weeks as the user requires.

# declare variables
totalBottles = 0 # stores accumulated bottle values
counter = 0 # controls the loop
todayBottles = 0 # stores number of bottles returned on a day
totalPayout = 0 # stores calculated value of totalBottles times .10
keepGoing = 'y' # used to run the program again
NBR_OF_DAYS = 7 # stores number of days in the week

# begins while loop, asking user for todayBottles input
while keepGoing == 'y':
    counter += 1
    print("Enter number of bottles returned for day #" + str(counter) + ":", end =' ')
    todayBottles = int(input())
    totalBottles = totalBottles + todayBottles

    # calculates payout once a week's worth of data has been entered
    if counter == 7:
        PAYOUT_PER_BOTTLE = .10
        totalPayout = 0 # resets to 0 for multiple runs
        totalPayout = totalBottles * .10

        # prints total bottles and payout for those bottles
        print('\nThe total number of bottles collected is ' + str(totalBottles))
        print('The total paid out is $' + str(f'{totalPayout:.2f}'))
        print("\nDo you want to enter another week’s worth of data?")
        print("(Enter y or n)", end =' ')
        keepGoing = input()
        print()
        counter = 0 # resets counter before looping back through



