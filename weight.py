"""This is to convert weight"""
import os

# age = 20
# price = 19.55
# first_name = "tyron"
# is_online = False
# print(first_name)
# name = input("What is your name? ")
# print("hello " + name)
# birth_year = input("Enter your birth year: ")
# age = 2023 - int(birth_year)
# print(age)
# first_number = float(input("First: "))
# second_number = float(input("Second: "))
# total = first_number + second_number
# print("answer is: " + str(total))
# course = "Python for Beginners"
# print("Python" in course)
# print(10 ** 3)
# x = 10
# x = x + 3
# x += 4
# print(x)
# x = 10 + 3 * 2
# x = 3 == 2
# print(x)
# price = 5
# print(not price > 10)
# temp = 5
# if temp > 30:
#    print("it's a hot day")
#    print("Drink plenty of water")
# elif temp > 20:
#    print("It's a nice day")
# elif temp > 10:
#    print("It's a bit cold")
# else:
#    print("it's cold")
# print("Done")

# weight = input("Weight : ")
# kilo = 2.04
# lbs = 0.45
# if weight > 0:
#    kgtolbs = input("Enter (K)ilo or (L)Pounds : ")
#    if kgtolbs == "k":
#        print("Your weight is: " + str(weight * 2.04) + " Pounds")
#    elif kgtolbs != "k":
#        print("Your weight is: " + str(weight * 0.45) + " Kilo")
# elif weight == str:
#    print("Error")
# else:
#   print("done")
# Correct Way
print("Weight Conversion kilo to pound and vice versa")
CONVERT = True
while CONVERT is True:
    weight = int(input("Enter Weight : "))
    unit = input("(K)ilo or (P)ound : ")
    if unit.upper() == "K":
        converted = weight / 0.45
        print(f"Your weight is {converted:.02f} pounds")
    else:
        converted = weight * 0.45
        print("Your weight is " + str(converted) + " Kilo")

    again = input("Try again? 'Y' or 'N': ").lower()
    os.system("cls" if os.name == "nt" else "clear")

    if again == "n":
        CONVERT = False
