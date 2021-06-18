# Classes and Objects

# all attributes and methods of the string class
print(dir(""))
print("\n")

# documentation for string class
help("")
print("\n")


# define class

class Apple:
    color = ""
    flavor = ""


a = Apple()
a.color = "red"
a.flavor = "sweet"

print("The apple is {} and {}".format(a.color, a.flavor))

golden = Apple()
golden.color = "yellow"
golden.flavor = "soft"

print("The apple is {} and {}".format(a.color, a.flavor))
print("\n")


class Flower:
    color = 'unknown'


rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print("\n")


# quiz

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with
    # different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    temp_you = you.apples
    temp_me = me.apples
    you.apples = temp_me
    me.apples = temp_you
    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    sum = you.ideas + me.ideas
    you.ideas = sum
    me.ideas = sum
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
print("\n")


# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()
    return_city.elevation = 0

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population > min_population and city1.elevation > return_city.elevation:
        return_city.name = city1.name
        return_city.country = city1.country
        return_city.elevation = city1.elevation
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population > min_population and city2.elevation > return_city.elevation:
        return_city.name = city2.name
        return_city.country = city2.country
        return_city.elevation = city2.elevation
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population > min_population and city3.elevation > return_city.elevation:
        return_city.name = city3.name
        return_city.country = city3.country
        return_city.elevation = city3.elevation

    # Format the return string
    if return_city.name:
        return return_city.name + ", " + return_city.country
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""
print("\n")


class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return "This piece of furniture is made of {} {}".format(piece.color, piece.material)


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"
print("\n")


# instance methods

class Piglet:
    def speak(self):
        print("oink oink")


hamlet = Piglet()
hamlet.speak()
print("\n")


class Piglet:
    name = "piglet"

    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
print("\n")


class Piglet:
    years = 0

    def pig_years(self):
        return self.years * 18


piggy = Piglet()
print(piggy.pig_years())
piggy.years = 2
print(piggy.pig_years())
print("\n")


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())
print("\n")


# constructor

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


a = Apple("red", "sweet")
print(a.color)
print(a.flavor)

print(a)
print("\n")


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + self.name


# Create a new instance with a name of your choice
some_person = Person("Chris")
# Call the greeting method
print(some_person.greeting())
print("\n")


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)


a = Apple("red", "sweet")
print(a)
print("\n")

# documenting

help(Apple)
print("\n")


# docstrings

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds."""
    return hours * 3600 + minutes * 60 + seconds


help(to_seconds)
print("\n")


class Piglet:
    """Represents a piglet that can say their name"""
    years = 0
    name = ""

    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to the equivalent pig years."""
        return self.years * 18


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        """Outputs a message with the name of the person."""
        print("Hello! My name is {name}.".format(name=self.name))


help(Person)
print("\n")


# Jupyter Notebooks

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        return "Current floor: {}".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current != self.top:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current != self.bottom:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.top >= floor >= self.bottom:
            self.current = floor


elevator = Elevator(-1, 10, 0)

elevator.up()
print(elevator.current)  # should output 1

elevator.down()
print(elevator.current)  # should output 0

elevator.go_to(10)
print(elevator.current)  # should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)
print("\n")


# inheritance

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)
print("\n")


class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))


class Piglet(Animal):
    sound = "Oink!"


class Cat(Animal):
    sound = "Meow!"


hamlet = Piglet("Hamlet")
patchy = Cat("Patchy")

hamlet.speak()
patchy.speak()
print("\n")


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def check_material(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.check_material()
print("\n")


# composition

class Repository:
    def __init__(self):
        self.packages = {}  # empty dictionary of packages

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def stock_by_material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class Shirt(Clothing):
    material = "Cotton"


class Pants(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
sweatpants = Pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.stock_by_material("Cotton")
print(current_stock)
print("\n")


# modules

import random

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print("\n")


import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now() + datetime.timedelta(days=28))
print("\n")


# Jupyter Notebook 2: Electric Boogaloo
