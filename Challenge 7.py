# Challenge 7: Check if a Number is Even or Odd
# Write a Python program that prompts the user to enter a
# number and checks if it's even or odd.


def IsEvenOrOdd(number):
    if number %2 == 0:
        print("Even")
    else:
        print("Odd")


number = int(input("Please Enter a Number: "))

IsEvenOrOdd(number)