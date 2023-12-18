'''import pandas as pd
df = pd.read_csv("bank_marketing.csv")
df = df.drop("Unnamed: 0", axis=1, errors="ignore")

df = df.dropna()

df = df.drop_duplicates()

shape_after_operations = df.shape
print(f"Shape of data after dropping 'Unnamed: 0', missing values, and duplicates: {shape_after_operations}")

average_age_subscribed = df[df['deposit'] == 'yes']['age'].mean()
print(f"Average age of clients who have subscribed to a deposit: {average_age_subscribed:.2f}")

def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

numerator = 10
denominator = 0

try:
    result = divide(numerator, denominator)
    print(f"Result: {result}")
except AssertionError as e:
    print(f"AssertionError: {e}")


class ZeroProductError(Exception):
    def __init__(self, message="The product of (b * d) is zero."):
        self.message = message
        super().__init__(self.message)

def calculate_product(b, d):
    result = b * d
    if result == 0:
        raise ZeroProductError()
    return result

try:
    b_value = 0
    d_value = 5
    product_result = calculate_product(b_value, d_value)
    print(f"The product of ({b_value} * {d_value}) is: {product_result}")
except ZeroProductError as e:
    print(f"Error: {e}")

class MarksExceedError(Exception):
    def __init__(self, message="Marks cannot exceed above 100"):
        self.message = message
        super().__init__(self.message)

def calmarks(math, python):
    total_marks = math + python
    if total_marks > 100:
        raise MarksExceedError()
    return total_marks

try:
    math = 90
    python = 90
    res = calmarks(math, python)
    print(f"Total Marks: {res}")
except MarksExceedError as e:
    print(f"ERROR!! {e}")


class BankAccount:
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.01):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def compute_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(f"Interest of ${interest_earned:.2f} earned and added to the balance.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

account_holder_name = input("Enter the account holder's name: ")
initial_balance = float(input("Enter the initial balance: "))
interest_rate = float(input("Enter the interest rate (e.g., 0.01 for 1%): "))

account1 = BankAccount(account_holder_name, initial_balance, interest_rate)

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Compute Interest")
    print("4. Display Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter the deposit amount: "))
        account1.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the withdrawal amount: "))
        account1.withdraw(amount)
    elif choice == '3':
        account1.compute_interest()
    elif choice == '4':
        account1.display_balance()
    elif choice == '5':
        print("Exiting the banking application.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter the factorial: "))
res=fact(num)
print(f"answer: {res}")

largest = lambda x, y: x if x > y else y

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = largest(num1, num2)
print(f"The largest of {num1} and {num2} is: {result}")


def calculate_arithmetic_mean(*values):
    if not values:
        return None
    return sum(values) / len(values)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

mean_result = calculate_arithmetic_mean(num1, num2, num3)
print(f"The arithmetic mean is: {mean_result}")


import numpy as np
array2d=np.array([[1,2,3],
[4,5,6],
[7,8,9]])
cols=np.sum(array2d,axis=0)
print(array2d)
print(cols)
#axis=1->rowwise
#axis=0->colwise


import numpy as np
array2d=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
array1d=array2d.flatten()
print(array1d)


import numpy as np
array = np.array([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 8, 9, 2, 1, 2, 3, 2, 4, 2])
unique_values, counts = np.unique(array, return_counts=True)
most_frequent_index = np.argmax(counts)
most_frequent_value = unique_values[most_frequent_index]

print("Original array:")
print(array)
print("\nMost frequent value:", most_frequent_value)

def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = []
    for i in range(len(matrix_a)):
        row = [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
        result.append(row)
    
    return result

def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix A must be equal to the number of rows in matrix B for multiplication.")
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            element_sum = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_a[0])))
            row.append(element_sum)
        result.append(row)
    
    return result

# Example matrices
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

# Add matrices
matrix_sum = add_matrices(matrix_a, matrix_b)

# Multiply matrices element-wise
matrix_product = multiply_matrices(matrix_a, matrix_b)

# Display the results
print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nMatrix Sum (A + B):")
for row in matrix_sum:
    print(row)

print("\nMatrix Product (A * B):")
for row in matrix_product:
    print(row)



import random

# Randomly select 10 integers from the range 100 to 200
random_integers = random.sample(range(100, 201), 10)

# Find the smallest among all
smallest_integer = min(random_integers)

# Display the selected integers and the smallest value
print("Randomly Selected Integers:")
print(random_integers)
print("\nThe Smallest Integer:", smallest_integer)



# Create a dictionary of 5 countries with currency details
countries_dict = {
    'USA': {'Currency': 'US Dollar', 'Symbol': '$'},
    'UK': {'Currency': 'British Pound', 'Symbol': '£'},
    'Japan': {'Currency': 'Japanese Yen', 'Symbol': '¥'},
    'India': {'Currency': 'Indian Rupee', 'Symbol': '₹'},
    'Australia': {'Currency': 'Australian Dollar', 'Symbol': 'A$'}
}

# Display the dictionary
print("Countries and Currency Details:")
for country, details in countries_dict.items():
    print(f"{country}: {details['Currency']} ({details['Symbol']})")



# Take a sentence as input
sentence = input("Enter a sentence: ")

# Replace each blank with a hyphen
modified_sentence = sentence.replace(' ', '-')

# Print the modified sentence
print("Modified Sentence:")
print(modified_sentence)


# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

# Specify the number of Fibonacci numbers to print
num_fibonacci = int(input("Enter the number of Fibonacci numbers to print: "))

# Print the specified number of Fibonacci numbers
print("Fibonacci Numbers:")
print(generate_fibonacci(num_fibonacci))

****importrandomnumbers=[random.randint(100,200) fori inrange(10)]
small =min(numbers)
print("Following numbers are:")print(numbers)***

***currency={"India":"Rupee" , "Europe":"Euro","America":"Dollars","UK":"Pounds"}
print("Dictionary is :")
print(currency)print(currency["India"])****

import numpy as np

# Create a NumPy array filled with all ones
ones_array = np.ones((3, 3))  # Specify the shape (3x3 in this example)

# Display the array
print("NumPy Array Filled with All Ones:")
print(ones_array)


import numpy as np

# Create a NumPy array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Specify a row to check
specified_row = np.array([4, 5, 6])

# Check whether the array contains the specified row
contains_specified_row = np.any(np.all(matrix == specified_row, axis=1))

# Display the result
print("Matrix:")
print(matrix)
print("\nDoes the Matrix Contain the Specified Row?", contains_specified_row)
'''

players = ["Neymar", "Ronaldo", "Messi" , "Mbappe", "Salah", "Kane", "Lewandowski", "De Bruyne", "Modric", "Kante"]
print("Original List:")
print(players)
players.sort()
print("\nSorted List:")
print(players)
player_to_remove = "Neymar"
if player_to_remove in players:
    players.remove(player_to_remove)
    print("\nList after removing", player_to_remove + ":")
    print(players)