#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("John")  # Passing a name argument when calling the function

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()  # Without passing any arguments, it will use the default value
greet_with_default("Alice")  # Passing a name argument overrides the default value

def add(num1, num2):
    return num1 + num2

print(add(2, 3))  # Calling the add function with two arguments and printing the result

def halve(number):
    return number / 2

print(halve(10))  # Calling the halve function with an argument and printing the result
