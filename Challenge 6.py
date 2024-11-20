# Challenge 6: Count Vowels in a String
# Write a Python program that prompts the user to enter a
# string and counts the number of vowels (a, e, i, o, u) in that string


def Count_vowels(String):
    count = 0
    for char in String:
        if char.lower() in 'aeiou':
            count += 1
    print (f"Number of vowels: {count}")
    

String = input("Enter a word: ")

Count_vowels(String)