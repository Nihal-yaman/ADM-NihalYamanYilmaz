# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")  # Print "Hello, World!" to the console

# Arithmetic Operators
if __name__ == '__main__':
    x = int(input())  # Read an integer input x
    y = int(input())  # Read an integer input y
    print(x + y)  # Print the sum of x and y
    print(x - y)  # Print the difference of x and y
    print(x * y)  # Print the product of x and y

# Python: Division
if __name__ == '__main__':
    x = int(input())  # Read an integer input x
    y = int(input())  # Read an integer input y
    print(x // y)  # Print the integer division of x by y
    print(x / y)  # Print the float division of x by y

# Loops
if __name__ == '__main__':
    n = int(input())  # Read an integer input n
    i = 0
while 1 <= n <= 20 and i < n:  # Loop from 0 to n-1
    print((i)**2)  # Print the square of the current value of i
    i += 1

# Write a function
def is_leap(year):
    # Return True if year is a leap year, else return False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

n = int(input())  # Read an integer input n
if n % 2 != 0:  # If n is odd
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:  # If n is even and in range [2, 5]
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:  # If n is even and in range [6, 20]
    print("Weird")
elif n % 2 == 0 and n > 20:  # If n is even and greater than 20
    print("Not Weird")

# Print Function
if __name__ == '__main__':
    n = int(input())  # Read an integer input n
for i in range(1, n + 1):  # Loop from 1 to n
    print(i, end='')  # Print i in the same line without spaces

# List Comprehensions
x = int(input())  # Read input x
y = int(input())  # Read input y
z = int(input())  # Read input z
n = int(input())  # Read input n
# List comprehension to generate the 3D coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# Print the resulting list
print(coordinates)

# Nested Lists
n = int(input())  # Read number of students
students = []  # Create an empty list to store the student records
# Collect student names and grades
for _ in range(n):
    name = input()  # Read student name
    grade = float(input())  # Read student grade
    students.append([name, grade])  # Store as a list [name, grade]
# Find the second lowest grade
grades = sorted(set([grade for name, grade in students]))  # Get unique grades and sort them
second_lowest_grade = grades[1]  # The second lowest grade
# Find the students who have the second lowest grade
second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]
# Sort names alphabetically
second_lowest_students.sort()
# Print the names of students with the second lowest grade
for name in second_lowest_students:
    print(name)

# Finding the percentage
if __name__ == "__main__":
    n = int(input())  # Read number of students
    student_marks = {}  # Dictionary to store student names and marks
    for _ in range(n):
        name, *line = input().split()  # Read student name and scores
        scores = list(map(float, line))  # Convert scores to float
        student_marks[name] = scores  # Store scores in dictionary
    query_name = input()  # Read the name to query
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])  # Calculate average score
    print(f"{avg_score:.2f}")  # Print the average score rounded to 2 decimal places

# Lists
lst = []  # Initialize an empty list
n = int(input())  # Read the number of commands
for _ in range(n):
    command = input().split()  # Read the command
    if command[0] == "insert":
        lst.insert(int(command[1]), int(command[2]))  # Insert value at specified index
    elif command[0] == "print":
        print(lst)  # Print the list
    elif command[0] == "remove":
        lst.remove(int(command[1]))  # Remove first occurrence of the value
    elif command[0] == "append":
        lst.append(int(command[1]))  # Append value to the list
    elif command[0] == "sort":
        lst.sort()  # Sort the list
    elif command[0] == "pop":
        lst.pop()  # Pop the last element
    elif command[0] == "reverse":
        lst.reverse()  # Reverse the list

# Tuples
n = int(input())  # Read the number of elements
integer_list = tuple(map(int, input().split()))  # Convert input to tuple
print(hash(integer_list))  # Print the hash of the tuple

# Find the Runner-Up Score!
n = int(input())  # Read the number of scores
scores = list(map(int, input().split()))  # Convert input to list of scores
unique_scores = list(set(scores))  # Remove duplicate scores
unique_scores.sort()  # Sort the unique scores
print(unique_scores[-2])  # Print the second highest score
