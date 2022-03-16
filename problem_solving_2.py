# Happy Numbers 
# a happy number is a number defined by the following process: starting with any positive integer
# Replace the number by the sum of the squares of its digits
# Repeat the process until the number equals 1. 
# Write a method that determines if a number is happy or sad 
number = "19"
first = int(number[0])
second = int(number[1])
equation = (first ** 2) + (second ** 2)
print(equation)