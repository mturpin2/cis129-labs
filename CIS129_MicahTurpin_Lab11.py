# CIS129 Module 11 Lab
# Author: Micah Turpin
# 5/7/2024


# 9.1 (CLASS AVERAGE: WRITING GRADES TO A PLAIN TEXT FILE)
    # Figure 3.2 presented a class-average script in which you could enter any number
    # of grades followed by a sentinel value, then calculate the class average. Another
    # approach would be to read the grades from a file. In an IPython session, write
    # code that enables you to store any number of grades into a grades.txt plain text file.

with open('grades.txt', 'w') as grades:
# Opens the file in write mode
    while True:
        grade = input("Enter a grade (or 'quit' to stop): ")
        # Asks for a grade

        if grade.lower() == 'quit':
            break
        # If the user types 'quit', stops asking for more grades

        grades.write(grade + '\n')
        # Writes the grade to the file

print("Grades have been successfully written to grades.txt.")
# Confirms to user that grades have been written to text file


# 9.2 (CLASS AVERAGE: READING GRADES FROM A PLAIN TEXT FILE)
    # In an IPython session, write code that reads the grades from the grades.txt file
    # you created in the previous exercise. Display the individual grades and their
    # total, count and average.

with open('grades.txt', 'r') as file:
    grades = file.readlines()
# Opens the file in read mode

grades = [int(grade.strip()) for grade in grades]
# Removes newline characters and converts grades input to integers

total = sum(grades)
count = len(grades)
average = total / count
# Calculates total, count, and average

print("Individual Grades: ", grades)
print("Total: ", total)
print("Count: ", count)
print("Average: ", average)
# Prints individual grades, total combined grades, amount of grades recorded, and average of all the grades


# 9.3 (CLASS AVERAGE: WRITING STUDENT RECORDS TO A CSV FILE)
    # An instructor teaches a class in which each student takes three exams. The instructor
    # would like to store this information in a file named grades.csv for later use. Write
    # code that enables an instructor to enter each student’s first name and last name as
    # strings and the student’s three exam grades as integers. Use the csv module to write
    # each record into the grades.csv file. Each record should be a single line of text in
    # the following CSV format:
        # firstname,lastname,exam1grade,exam2grade,exam3grade

import csv

with open('grades.csv', 'w', newline='') as grades:
# Opens the file in write mode
    writer = csv.writer(grades)
    while True:
        first_name = input("Enter the student's first name (or 'quit' to stop): ")
        # Ask for student first name

        if first_name.lower() == 'quit':
            break
            # If the user types 'quit', the script stops asking for more student details
        last_name = input("Enter the student's last name: ")
        exam1grade = int(input("Enter the student's first exam grade: "))
        exam2grade = int(input("Enter the student's second exam grade: "))
        exam3grade = int(input("Enter the student's third exam grade: "))
        # Assigns user inputted values to student detail variables
        # Converts grade inputs to integers as a form of input validation

        writer.writerow([first_name, last_name, exam1grade, exam2grade, exam3grade])
        # Write the student details to the file

print("Student records have been successfully written to grades.csv.")
# Confirms to user that student records have been updated in grades.csv file
