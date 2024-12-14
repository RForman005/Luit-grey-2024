import random  # Importing the random module to generate random numbers

number = random.randint(0, 10)  # Generating a random integer between 0 and 10 (inclusive)

print(number)  # Printing the generated random number to the console

import math

# Calculate the square root of a number
print(math.sqrt(16))  # Output: 4.0

# Calculate the value of pi
print(math.pi)  # Output: 3.141592653589793

import random

# Pick a random number between 1 and 100
print(random.randint(1, 100))

# Pick a random item from a list
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))

from datetime import datetime

# Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}")

import os

# Get the current working directory
print(os.getcwd())

# List files in the current directory
print(os.listdir())

import matplotlib.pyplot as plt

# Simple plot of y = x^2
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

plt.plot(x, y, marker='o')  # Create a line plot with markers
plt.title("Graph of y = x^2")  # Add a title
plt.xlabel("x")  # Label x-axis
plt.ylabel("y")  # Label y-axis
plt.grid(True)  # Add a grid
plt.show()  # Display the plot

import time

start = time.time()
# Some time-consuming operation
time.sleep(2)  # Pause for 2 seconds
end = time.time()

print(f"Execution time: {end - start} seconds")

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output the status code of the request
print(response.json())  # Output the JSON data from the response

