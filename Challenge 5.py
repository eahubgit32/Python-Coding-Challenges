# Challenge 5: Reverse a String
# Write a Python program that prompts the user to enter a
# string and then prints the reverse of that string.


def ReverseString(String):
    print("Reversed String: " + String[::-1]) #[::-1] is a method that reverse a string


String = input("Enter a word to be reversed: ")

ReverseString(String)