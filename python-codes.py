'''
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {calculate_factorial(number)}")

def rev_string(s):
    return s[::-1]
s=input("enter a string: ")
print(f"{rev_string(s)}")

def find_largest_smallest(arr):
    if not arr:
        return None, None
    else:
        return max(arr), min(arr)

array = [int(x) for x in input("Enter integers: ").split(',')]
largest, smallest = find_largest_smallest(array)
print(f"Largest: {largest}, Smallest: {smallest}")

def is_palindrome(input_str):
    return input_str == input_str[::-1]
word = input("Enter a string: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result_dict = merge_dictionaries(dict1, dict2)
print(f"Merged Dictionary: {result_dict}")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(4, 5)
print(f"Area: {rectangle.calculate_area()}, Perimeter: {rectangle.calculate_perimeter()}")


import numpy as np
matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)
print(f"Original Matrix:\n{matrix}")
print(f"Inverse Matrix:\n{inverse_matrix}")

--

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {result}")



def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits(number)}")--

try:
    result = 10 / 0
except (ZeroDivisionError, ArithmeticError) as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"Caught an exception: {e}")


import numpy as np

array = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
sorted_array = np.sort(array)

print(f"Original Array: {array}")
print(f"Sorted Array: {sorted_array}")

import pandas as pd

# Example DataFrames (Replace these with your actual DataFrames)
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'C': [7, 8, 9], 'D': [10, 11, 12]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged_df = pd.concat([df1, df2], axis=1)
print("Merged DataFrame:")
print(merged_df)
'''
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

number = abs(int(input("Enter a number: ")))  # Use abs to handle negative numbers
print(f"Sum of digits: {sum_of_digits(number)}")
