# While loops
'''
x = 0
while x < 5:
    print("Not there yet, x = " + str(x))
    x = x + 1
print("x = " + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


var = 1
sum = 0
while var < 10:
    sum += var
    var += 1
print("Sum:" + str(sum) + ", " + "Var:" + str(var))


x = 100
while x != 0 and x % 2 == 0:
    x = x / 2
print(x)


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)


'''

# For loops
'''
for x in range(5):
    print(x)
print("\n")


friends = ['Rob', 'Ian', 'Sid', 'Andrew']
for friend in friends:
    print("Hi " + friend)
print("\n")


values = [23, 52, 59, 37, 48]
sum = 0
len = 0
for val in values:
    sum += val
    len += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum / len))
print("\n")


product = 1
for n in range(1, 10):
    product = product * n

print(product, end="\n")


def to_cel(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print(x, to_cel(x))
print("\n")


# NESTED FOR LOOPS

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
print("\n")


teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
print("\n")


# COMMON ERRORS

# for x in 25:
for x in range(25):
    print(x)
print("\n")


for x in [25]:
    print(x)
print("\n")


def greet_friends(f):
    for frnd in [f]:            # <- convert to list, not just "for frnd in f:"
        print("Hi " + frnd)


f = ['Rob', 'Ian', 'Sid', 'Andrew']
greet_friends("Bailey")
print("\n")


def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n+1))
print("\n")

'''

# Recursion
'''


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


print(factorial(4))
# print(factorial(998))


def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)


'''

# Exam
'''
def digits(n):
    count = 0
    if n == 0:
        return 1
    while n >= 1:
        count += 1
        n = n / 10
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1


def multiplication_table(start, stop):
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

'''
