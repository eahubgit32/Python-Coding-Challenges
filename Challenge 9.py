# Challenge 9: Check if a Number is Prime
# Write a Python program that prompts the user to enter a
# number and checks if it's a prime number.

import math

def isPrime(number):
    if number > 1:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                print("Is not Prime")
            else:
                print("Prime")



number = int(input("Enter a number"))

isPrime(number)