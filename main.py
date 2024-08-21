# print('I love pizza')
# print("it's really good!")
# first_name = "Dewunmi"
# last_name ="Adesanya"
# full_name = first_name + " " +last_name
# print("Hello " +full_name)
# print(type(name))
# age = 21
# age += 1
#print(age)
# print("Your age is: "+str(age))
# height = 250.5
# print("your height is: "+str(height)+"cm")
# print(type(height))
# name = "dewunmi adesanya"
# print(len(name))
# print(name.find("e"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("e"))
# print(name.replace("e", "a"))
# print(name*5)
# x = 1
# y = 2.0
# z = "3"
#
# x = float(x)
# y = int(y)
# z = float(z)
#
# print(x*5)
# print(y*5)
# print(z*5)
# name = input("what is your name?: ")
# age = int(input("how old are you?: "))
# height = float(input("how tall are you?: "))
# print("hello " +name)
# print("you are " +str(age))
# print("you are " +str(height))

# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(100))
# print (max(x,y,z))
# print (min(x,y,z))

# name = "Bro code "
# First_name = name[:3]
# last_name = name[4:8]
# funky_name = name[::3]
# reversed_name = name[::-1]
# print(First_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)
#
# website1 = "https//google.com"
# website2 = "https//wikipedia.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])
# age = int(input("How old are you?: "))
# if age >= 18:
#     print("you are an adult!")
# elif age < 0:
#     print("you haven't been born yet!")
# else:
#     print("you are a child!")

# temp = int(input("what is the temperature outside?: "))
# if temp >= 0 and temp <= 30:
#     print("the temperature is good today!")
#     print("go outside!")
# elif temp < 0 or temp > 30:
#     print("the temperature is bad today!")
#     print("stay inside!")
# name = None
#
# while not name:
#     name = input("Enter your name: ")
#
# print("Hello "+name)

# for i in range(10):
#     print(i+1)
# for i in range(50,100+1,2):
#     print(i)
# for i in "Bro code":
#     print(i)
# name = "John smith"
# age = 20
# new_patient = True
# input(age)

# name = input('What is your name?: ')
# color = input('What is your favourite color?: ')
# print(name +" likes "+ color)
# weight = input("weight(lbs)?: ")
# weight_kg = float(weight) * 0.45
# print(weight_kg)
# first ="john"
# last = "smith"
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)
# price = 1000000
# good_credit = True
# good_deal = False
# if good_credit:
#     payment = 0.1 * price
#     print("You need to put down 10%")
# elif good_deal:
#     payment = 0.2 * price
#     print("You need to put down 20%")
# print(f"Down payment:${payment}")
# has_high_income = True
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("eligible for loan")
# has_high_income = True
# has_good_credit = False
# if has_high_income or has_good_credit:
#     print("eligible for loan")
# has_high_income = True
# has_criminal_record = True
# if has_high_income and not has_criminal_record:
#     print("eligible for loan")
# temperature = 30
# if temperature > 30:
#     print("it's a hot day")
# elif temperature < 10:
#     print("it's a cold day")
# else:
#     print("it's neither hot nor cold")
# name = input("what is your name?: ")
# if (len(name)) < 3:
#     print("name must be at least 3 characters")
# elif (len(name)) > 50:
#     print("name must be a maximum of 50 characters")
# else:
#     print("looks good!")
# weight = input("weight(lbs)?: ")
# weight = input("weight: ")
# weight_size = input("(L)bs or (K)g: ")
# print(weight)
# print(weight_size)
# weight_lb = int(weight) * 0.45
# weight_kg = float(weight) * 2.20
# if weight_size == "l":
#     print("You're are " +str(weight_lb) +" kilogram")
# elif weight_size == "k":
#     print("You're are " +str(weight_kg) +" pounds")
# else:
#     print("enter l or k")
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
#     print("Done")
# secret_number = 9
# count = 0
# limit = 3
# while count < limit:
#     guess = int(input('Guess: '))
#     count += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else:
#     print("sorry you failed")
# command = ""
# car_started = False
# while True:
#     command = input("> ").lower()
#
#     if command == "start":
#         if car_started:
#             print("car is already started")
#         else:
#             car_started = True
#             print("Car started...")
#     elif command == "stop":
#         if not car_started:
#             print("car is already stopped.")
#         else:
#             car_started = False
#             print("Car stopped")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry, I don't understand the code")

# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total += item
#     print(f"Total: {total}")

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
#
# for item in numbers:
#     print ('x' * item)
# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     output = ''
#     for i in range(item):
#         output += 'x'
#         print(output)
# numbers = [1, 2, 3, 4, 5]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# for i in range(11):
#     for j in range(1, 11):
#        print(f"{i} * {j} = {i*j}", end="\t")
#        print()
# for x in range(13):
#     for y in range(0, 13):
#         print(f"{x} * {y} = {x*y}", end="\t")
#         print()
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# del thislist
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if "a" in x]
#
# print(newlist)
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# Convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)
# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = thisdict.keys()
#
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.keys()
#
# print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = thisdict.values()
#
# print(x)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = thisdict.items()

# print(x)
#
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)
# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes")
# my_function("Adewunmi", "Adesanya")
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")
# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)
# def my_function(x):
#   return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# def myfunc(n):
#   return lambda a : a * n
#
# mytripler = myfunc(3)
#
# print(mytripler(11))
#
# x = lambda a: a + 10
# print(x(5))

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😄",
#         ":(": "😓"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
# message = input(">")
# print(emoji_converter(message))

# def square(number):
#     return(number * number)
#
#
# print(square(3))

# def name(first_name, last_name, age, job):
#     print("your name is " +first_name +" "+last_name)
#     print("you're " +str(age) +"years old")
#     print("you're a " +job)
#
#
# name("adepoju", "oguniran", 35, "lawyer")

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("you can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("enter only numbers please")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("this will always execute")

# import os
# path = "C:\\Users\DARE DANIEL\\OneDrive\\Pictures\\htmlcss course"
#
# if os.path.exists(path):
#     print("the location exists!")
#     if os.path.isfile(path):
#         print("this is a file")
#     elif os.path.isdir(path):
#         print("this is a directory")
# else:
#     print("that location doesn't exist!")

# with open('C:\\Users\DARE DANIEL\\OneDrive\\Pictures\\htmlcss course')as file:
#     print(file.read())

# text = "Have a nice day! See ya"
#appending new words is "a" while just written a new file is "w"

# with open('test.py', 'a') as file:
#     file.write(text)

# import shutil
# shutil.copyfile('test.py', 'copy.py')

# import os
# source = "test.py"
# destination = "C:\\Users\\DARE DANIEL\\OneDrive\\Desktop"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")

# import os
#
# path = "test.py"
#
# os.remove(path)

# import random
# while True:
#     choices = ["rock", "paper", "scissors"]
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()
#
#     if player == computer:
#         print("computer: ", computer)
#         print("player: ", player)
#         print("tie!")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you win!")
#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you win!")
#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("you win!")
#     play_again = input("play again? (yes/no): ").lower()
#
#     if play_again != "yes":
#         break
#
# print("bye!")

# abc = {1, 2, 3, 4, 5, 6, 7}
# ghi = iter(abc)
# print(next(ghi))
# print(next(ghi))
# print(next(ghi))
# print(next(ghi))
# print(next(ghi))
# print(next(ghi))
# print(next(ghi))
# for x in abc:
#     print(x)

# import datetime
#
# x = datetime.datetime.now()
#
# print(x)
#
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
#
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
#print(z)

#x = 'orange'
# y = 'banana'
# z = 'cherry'
# print (x, y, z)

# x = "lexus"
# y = 120
# print(type(x))
# print(type(y))
#
# i = 20.2
# j = True
# print(type(i))
# print(type(j))
#
# a = ''' hello it was nice to meet you
#
# yours sincerely
# dewunmi
#
# '''

# print(a)

# b = input("what is your name? ")
# print(b)

# fname = input("what is your first name? ")
# lname = input("what is your last name? ")
# age = input("how old are you? ")
# city = input("what city do you live? ")
# print("Hello good evening " + fname + " " + lname)
# print("You're " + age + " years old")
# print("you live in " + city)
# print("Amazing!")
#
#
# height = input("what is the height of the rectangle? ")
# width = input("what is the width of the rectangle? ")
# print(int(height) * int(width))
# print(help("requests"))
# x = "Good music "
# y = "coding"
# print(f"{x} and {y} = Happy coding!")