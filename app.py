
# Example one: 
def func(): 
    name = input('What is your name? ')
    color = input('What is your favourite color?')
    print(name + ' likes ' + color)


#  When using two different data types, you need to coerce one of them to be of the same type of the other
def difTyp():
    age = 2019 
    print(age)
    print(type(age))
    print(age)

# Ask a user their weight(in pounds), convert it to kilograms and print on the terminal
def weiTyp():
    weight_lbs = input("how much do you weight in pounds")
    weight_kg = int(weight_lbs) // 2.2
    print(weight_kg)


def courseTyp():    
    name = 'Jennifer'
    print(name[1:-1]) ## Give the character range you want
    first = 'John'
    last = 'Smith'
    message = first + '[ ' + last + '] is a coder'
    msg = f'{first} [{last}] is a coder' ## use f' for formatted strings and use curly brackets to dynamically insert values..
    print(msg)
    print(message)

def x():
    course = 'Python for Beginners'
    print(len(course))
    print(course.upper()) ## make all characters uppercase
    print(course.lower()) ## make all characters uppercase
    print(course.find('o')) ## find what index the letter o is, if you cant find the character the function returns -1"
    print(course.replace('P','J'))

x = 2 ** 2 ## exponentiation...\
print(round(x))
print(abs(-2.9))



# Weight converter App
# always indent in python with 4 spaces instead of 2..
def weightConv():
    weight = int(input("What is your Weight??"))
    unit = input("What is your unit of measurement(lbs or kg)")
    if unit.upper() == "L":
      conversion = weight * 0.45
      print(f"You are {conversion} kilos") # We use the formatted string to input dynamic values seamlessly to the string...
    else:
      conversion = weight / 0.45
      print(f"You are {conversion} pounds")



# Loops
def loops():
    i = 1
    while i <= 5:
        print('*' * i)
        i = i + 1
    print("Done")


# Generate a Random Number....

import random

# There is no such thing as do while loops in python, you need to enhance your while loop in order replicate that type of functionality...
secret_number = int(random.random() * 10) + 1
guess = 0
while secret_number != guess:
  guess = int(input('Guess: '))
  if guess == secret_number:
    print('You won!')
    break
  elif guess > secret_number:
    print("Go lower!!")
  else: 
    print("Go higher!!")

for item in [1,2,3,4,5,6,7,8]:
    print(item)

for item in range(10): 
  print(item)




# prices = [10 , 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")
# item  = [1,2,3,4,5,6,7,8,9]
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y}')


# numbers = (1,2,3) # using parenthesis makes this from a list to a tuple...
# print(numbers[0]) 
# numbers[0] = 10 # CANT DO this , tuples are immutable.. you going to get an error..
# print(numbers[0])

# coordinates = (1,2,3)
# coordinates[0] * coordinates[1] * coordinates[2]

# # First Version
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# # Second Version, cleaner code for readability
# x , y, z = coordinates


# customer = {
#     "name":"John Smith",
#     "age": 30,
#     "age": 40,
#     "is_verified": True
# }
# customer["name"] = "Jack Smith"
# print(customer.get("birthdate"))

# phone = input("Phone: ")
# digits_mapping = {
# "1":"One",
# "2":"Two",
# "3":"Three",
# "4":"Four",
# }

# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)


# Example 1: Create a game where you print out emojis using the dictionary
# message = input(">>")
# words = message.split(' ') # This string is being split into an list
# print(words)
# emojis  = {
#     ":)":"🆗",
#     ":(":"🆘"
# }
# output = ""
# for word in words:
#   output += emojis.get(word,word) + " "
# print(output)


# Introduction to functions...
# def greet_user():
#   print('Hi there!')
#   print("Welcome aboard")


# print("Start")
# greet_user()
# print("Finish")


# Exceptions
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#    print("Age cannot be 0.")
# except ValueError:
#    print('Invalid value')

# Different types in python: Number, Boolean, String,List, Dictionaries, Classes

# Classes
# class Point:
#    def __init__(self,x,y): # underscores to avoid naming conflicts with python keywords...
#       self.x = x
#       self.y = y
#    def move(self):
#       print("move")
#    def draw(self):
#       print("draw")

   
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)
# point2.move();

# class Person: 
#    def __init__(self,name): # We use init to identify a constructor
#       self.name = name
#    def talk(self):
#       print("I like to talk")


# person = Person("Warsame Osman")
# print(person.name)
# person.talk()

# # Inheritance

# class Mammal: 
#     def walk(self):
#         print("walk")

# class Dog(Mammal):
#     pass # Do Nothing

# class Cat(Mammal):
#     pass
