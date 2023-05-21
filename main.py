"""
a = 2
b = 3
c = a + b
c = 1
print(c)

myAge = 47
myName = "Joung"

print("Hello! my name is", myName)
print("and I'm ",myAge, "years old.")

dead = False
print(dead, "What?", 100)



def sayHello(user_name):     
    print("Hello", user_name, "How R U?")

sayHello("Joung")

sayHello("Nico")
sayHello("Kim")

def sayBye():
    print("Bye Bye!")

    sayHello()

def sayHello(user_name, user_age):     
    print("Hello", user_name, "How R U?")
    print("YOur age is", user_age, "years old. right?")

sayHello("Joung", 12)

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def tax_calculator(money):
    print(money * 0.35)

tax_calculator(1500000000)

def say_hello(user_name="anonymous"):
    print("hello", user_name)

say_hello("Joung")
say_hello()

def plus(a, b):
    print(a + b)

def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)

my_name = "Joung"
my_age = 12
my_color_eyes = "black"

print(f"Hello I'm {my_name}, I have {my_age} years in the earth, \
{my_color_eyes} is my eye color.")

def make_juice(fruit):
    return f"{fruit} + 🥤"
    print("this is invisible")

def add_ice(juice):
    return f"{juice} + 🧊"

def add_sugar(iced_juice):
    return f"{iced_juice} + 🍭"

juice = make_juice("🍎")
print(juice)
cold_juice = add_ice(juice)
print(cold_juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)

if 10 < 5:
    print("correct!")

if 10 == 10:
    print("True!")

a = "Joung"

if a == "Joung":
    print("True!")

password_correct = False

if password_correct:
    print("Here is your money")
else:
    print("Wrong password")

winner = 500

if winner <= 10:
    print("if")
elif winner <= 25:
    print("elif 1")
elif winner == 0:
    print("elif 2")
elif winner == 50:
    print("elif 3")
else:
    print("else")

age = int(input("how old are you?"))
print("User answer", age)
print(type(age))

if age < 18:
    print("You can't drink!")
elif age >= 18 and age <=35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Let's party!")
else:
    print("Go ahead!")

distance = 0

while distance < 20:
    print("I'm runnning", distance, "km")
    distance = distance + 1
"""
from random import randint, random

print("Welcome to Python Casino")
pc_choice = randint(1, 10) 

playing = True

while playing:
    user_choice = int(input("Choose number(1 ~ 10) :"))

    if user_choice == pc_choice:
        print("You win!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")

