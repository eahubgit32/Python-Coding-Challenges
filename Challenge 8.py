# Challenge 8: Find the Maximum of Two Numbers
# Write a Python program that prompts the user to enter two
# numbers and finds the maximum of the two



def Maxmium(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))


print("The Maximum Number is:", Maxmium(number1, number2))

#Another Approach

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))


maximum = max(num1, num2)

print(f"The Maximum Numbere is: {maximum}")