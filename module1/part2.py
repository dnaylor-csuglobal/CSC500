"""
Write a Python program to find the multiplication and division of two numbers.

Ask the user to input two numbers (num1 and num2).
Given those two numbers, multiply them together to find the output.
Also, divide num1/num2 to find the output.
"""


def read_int():
    while True:
        try:
            return int(input())
        except:
            print("Input is not a valid number. Please try again: ")


def read_nonzero_int():
    while True:
        num = read_int()
        if num != 0:
            return num
        else:
            print("Input must be non-zero. Please try again: ")


print("Please input the first number: ")
num1 = read_int()
print("Please input a non-zero number for the second number: ")
num2 = read_nonzero_int()
print(f"The product of {num1} and {num2} is {num1 * num2}")
print(f"The quotient of {num1} and {num2} is {num1 / num2}")
