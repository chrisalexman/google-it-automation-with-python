# data types / structures
# strings, lists, dictionaries

# strings
name = "Sasha"
color = 'blue'
pet = ""

print("Name: " + name + ", Color: " + color)
print(color * 3)
print(len(color))
print("\n")


# ex 1
def double_word(word):
    return word * 2 + str(len(word * 2))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0
print("\n")


# ex 2
name = "Sasha"
print(name[0])
print(name[1])
print(name[4] + "\n")

text = "Random string, lots of characters"
print(text[-1])
print(text[-2] + "\n")


# ex 3
def first_and_last(message):
    if len(message) == 0:
        return True
    if message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
print("\n")


# ex 4
# slice, substring
color = "Orange"
print(color[1:4])

fruit = "Pineapple"
print(fruit[:4])

fruit = "Mangosteen"
print(fruit[:5] + fruit[5:] + "\n")


# ex 5
message = "A oong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

print("Dragons" in pets)
print("Cats" in pets)
print("\n")


# ex 5
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


animals = "lions tigers and bears"
print(len(animals))
print(animals.index("g"))
print(animals.index("b"))
print(animals.index("bears"))
print("horses" in animals)
print("tigers" in animals)
print("\n")


# ex 6
print("Mountains".upper())
print("Mountains".lower())

answer = 'YES'
if answer.lower() == 'yes':
    print("User said yes")

print(" spaces ".strip())
print(" spaces ".lstrip())
print(" spaces ".rstrip())

print("How many times e is in the string:", "The number of times e occurs in this string is:".count("e"))

print("Does Forest end with rest? ", "Forest".endswith("rest"))

print("Is 12345 numeric? ", "12345".isnumeric())

print(int("12345") + int("54321"))

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces", "!"]))

print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots", "!"]))

print("This is another example".split())


# ex 7
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS
print("\n")


# ex 8
name = "Sasha"
number = len(name) * 4
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*4))
print("\n")


# ex 9
def student_grade(name, grade):
    return "{name} received {grade}% on the exam".format(name=name, grade=grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
print("\n")


# ex 10
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))
print("\n")


# ex 11
def to_celsius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
print("\n")


# ex 12
def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for x in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if x != " ":
            new_string = new_string + x.lower()
            reverse_string = x.lower() + reverse_string
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
print("\n")


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km
print("\n")


weather = "Rainfall"
print(weather[:4])
print("\n")


def nametag(first_name, last_name):
    return "{} {}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."
print("\n")


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
print("\n")


####

# list

x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print(len(x))
print("are" in x)
print("Today" in x)
print(x[0] + "..." + x[3])
print(x[1:3])
print(x[:2])
print(x[2:])
print("\n")


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n-1]
    return ""


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing
print("\n")


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(fruits)
fruits.append("Kiwi")
print(fruits)
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(32, "Peach")
print(fruits)

fruits.remove("Melon")
print(fruits)
print(fruits.pop(3))
print(fruits)
fruits[2] = "Strawberry"
print(fruits)
print("\n")


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for e in elements:
        # Does this element belong in the resulting list?
        if (i % 2) == 0:
            # Add this element to the resulting list
            new_list.append(e)
            # Increment i
        i += 1

    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []
print("\n")


# tuples

fullname = ('Sasha', 'S', 'Hopper')
print(fullname)
print("\n")


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(result)
print(type(result))

h, m, s = result
print(h, m, s)

h, m, s = convert_seconds(1000)
print(h, m, s)
print("\n")


def file_size(file_info):
    name, type, size = file_info
    return "{:.2f}".format(size / 1024)


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21
print("\n")


animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0

for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
print("\n")


winners = ["Ashley", "Laura", "Marisha"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
print("\n")


def skip_elements(elements):
    new_list = []
    for index, elem in enumerate(elements):
        if index % 2 == 0:
            new_list.append(elem)

    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
# Should be ['Orange', 'Strawberry', 'Peach']
print("\n")


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([("matt@example.com", "Matt Miller"), ("liam@example.com", "Liam O'Brien")]))
print("\n")


multiples = []
for x in range(1, 11):
    multiples.append(x * 7)

print(multiples)

multiples = [x * 7 for x in range(1, 11)]
print(multiples)
print("\n")


languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
print("\n")


z = [x for x in range(0, 101) if x % 3 == 0]
print(z)
print("\n")


def odd_numbers(n):
    return [x for x in range(0, n+1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []
print("\n")


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [file[:-2] if file.endswith(".hpp") else file for file in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
print("\n")


def pig_latin(text):
    say = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say.append(word[1:] + word[0] + "ay")
        # Turn the list back into a phrase
    return " ".join(say)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
print("\n")


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------
print("\n")


def group_list(group, users):
    members = ", ".join(users)
    return group + ": " + members


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"
print("\n")


def guest_list(guests):
    for name, age, job in guests:
        print("{} is {} years old and works as {}".format(name, age, job))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
print("\n")


# dictionary

x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)

file_counts["cfg"] = 8
print(file_counts)

file_counts["csv"] = 17
print(file_counts)

del file_counts["cfg"]
print(file_counts)
print("\n")


toc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25 , "Chapter 4": 30}
toc["Epilogue"] = 39  # Epilogue starts on page 39
toc["Chapter 3"] = 24  # Chapter 3 now starts on page 24
print(toc)  # What are the current contents of the dictionary?
print("Chapter 5" in toc)  # Is there a Chapter 5?
print("\n")


file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extensions in file_counts:
    print(extensions)

for ext, amnt in file_counts.items():
    print("There are {} files with the .{}".format(amnt, ext))

print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
    print(value)

print("\n")


cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, thing in cool_beasts.items():
    print("{} have {}".format(beast, thing))
print("\n")


def count_letters(text):
    result  = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long striwith a lot of letters"))
print("\n")


wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for item, color in wardrobe.items():
    for c in color:
        print("{} {}".format(c, item))
print("\n")


def email_list(domains):
    emails = []
    for email_ending, users in domains.items():
        for user in users:
            emails.append(user + "@" + email_ending)
    return emails


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                  "yahoo.com": ["barbara.gordon", "jean.grey"],
                  "hotmail.com": ["bruce.wayne"]}))
print("\n")


def groups_per_user(group_dictionary):
    user_groups = {}
    user_list = [[], [], []]
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user == "admin":
                user_list[0].append(group)
            if user == "userA":
                user_list[1].append(group)
            if user == "userB":
                user_list[2].append(group)
    user_groups["admin"] = user_list[0]
    user_groups["userA"] = user_list[1]
    user_groups["userB"] = user_list[2]
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))
print("\n")


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
print("\n")


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for item, cost in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += cost
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44
print("\n")


# quiz

def format_address(address_string):
    # Declare variables
    text = []
    house_number = 0
    street_name = []
    # Separate the address string into parts
    text = address_string.split()
    # Traverse through the address parts
    for word in text:
        # Determine if the address part is the
        # house number or part of the street name
        if word.isnumeric():
            house_number = word
        else:
            street_name.append(word)
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, " ".join(street_name))


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

print("\n")


def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
print("\n")


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    jamies_rev = list1[::-1]
    new_list = list2 + jamies_rev

    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
print("\n")


def squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("\n")


def car_listing(car_prices):
    result = ""
    for type, cost in car_prices.items():
        result += "{} costs {} dollars".format(type, cost) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
                   "Ford Fiesta": 13000, "Toyota Prius": 24000}))
print("\n")


def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    guest = {}
    for person, invites in guests2.items():
        guest[person] = invites
    for person, invites in guests1.items():
        guest[person] = invites
    return guest


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, 
                 "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, 
                   "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))
print("\n")


def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter.isalpha():
            # Add or increment the value in the dictionary
            if letter.lower() not in result:
                result[letter.lower()] = 1
            else:
                result[letter.lower()] += 1
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

print("\n")


animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
print("\n")


colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
print("\n")


host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())
print("\n")
