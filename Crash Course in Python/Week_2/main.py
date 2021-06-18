# Data Types

x = 2.5
print(type(x))
print("\n")


# Expressions

length = 10
width = 5
area = length * width
print(area)
print("\n")


# Expressions, Numbers, and Type Conversions

print(7 + 8.5)                      # implicit conversion
print("a" + "b" + "c")
print("\n")

base = 6
height = 3
area = (base * height) / 2
print("Area: " + str(area))         # explicit conversion
print("\n")

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is:" + str(average))
print("\n")

bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))
print("\n")


# Defining Functions

def greeting(name, dept):
    print("Welcome, " + name)
    print("You are part of " + dept)


greeting("Chris", "Parks Dept")
result = greeting("Andrew", "IT Dept")
print(result)
print("\n")


def get_seconds(hours, minutes, seconds):
    return 3600 * hours + 60 * minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)
print("\n")


def area_triangle(base, height):
    return (base * height) / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
the_sum = area_a + area_b
print("Sum is: " + str(the_sum))
print("\n")


def convert_seconds(sec):
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    remaining_seconds = sec - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
print("\n")


# Code Style

# 1. Self-Documenting: easy to read, understand
# 2. Refactoring: clear intent
# 3. Comment

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)


circle_area(5)
print("\n")


# Conditionals

# operations
print(10 > 1)

print("cat" == "dog")

print(1 != 2)

# print(1 < "1")  # error here

# keywords: and or not

print(1 == "1")

print("cat" > "Cat")

print("Yellow" > "Cyan" and "Brown" > "Magenta")        # alphabetical for strings, (T and F)

print(25 > 50 or 1 != 2)

print(not 42 == "Answer")

print("\n")


# branching

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else:
        print("Valid username.")


hint_username("Al")
hint_username("Edward")
hint_username("abcdefghijlmnopq")
print("\n")


def is_even(num):
    if num % 2 == 0:
        return True
    return False


result = is_even(3)
print(result)
result = is_even(4)
print(result)
print("\n")


# Module

print("big" > "small")


def thesum(x, y):
    return x + y


print(thesum(thesum(1, 2), thesum(3, 4)))

print((10 >= 5*2) and (10 <= 5*2))
