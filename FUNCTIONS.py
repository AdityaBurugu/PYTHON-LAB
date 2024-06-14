
# Calculator
import re
print("Calculator\n")
print("Type 'quit' to Exit")
previous = 0
run = True
def performmath():
    global run
    global previous
    equation = None

    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Good Bye")
        run = False
    else:
        equation = re.sub('[a-z A-Z , . :()""]', '', equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)
while run:
    performmath()


# Factorial using recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(int(input("Enter a Number:"))))

# Factorial using recursion lambda
fact = lambda n: 1 if n == 0 or n == 1 else n*fact(n-1)

print(fact(int(input("Enter a Number:"))))

# Duplicate elements in a List
def dups(arr):
    repeated = list()
    for ele in arr:
        if arr.count(ele) > 1 and ele not in repeated:
            repeated.append(ele)
    return repeated


arr = [1, 2, 3, 4, 5, 5, 6, 7, 3, 8, 9]
print(dups(arr))

# Unique elements in a List
def unique(arr):
    unique_list = list()
    for ele in arr:
        if arr.count(ele) == 1:
            unique_list.append(ele)
    return unique_list


arr = [1, 2, 3, 4, 5, 5, 6, 7, 3, 8, 9]
print(unique(arr))


# Cumulative Product of a List
def cumulative_product(arr):
    prod = 1
    for ele in arr:
        prod = prod * ele
    return prod


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cumulative_product(arr))

# Reverse of a List
def reverse(arr):
    return arr[::-1]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse(arr))

# Reverse of a List using lambda
reverse = lambda arr: arr[::-1]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse(arr))


# GCD of two Numbers
def gcd(a, b):
    GCD = None
    m = min(a, b)
    for i in range(1, m + 1):
        if a % i == 0 and b % i == 0:
            GCD = i
    return GCD


a = int(input("Ënter a Value:"))
b = int(input("Ënter b Value:"))
print(gcd(a, b))


# LCM of a Two Numbers
def lcm(a, b, gcd):
    return (a * b) / gcd


# LCM of Two Numbers using lambda
lambda_lcm = lambda a, b, gcd: (a * b) / gcd

a = int(input("Ënter a Value:"))
b = int(input("Ënter b Value:"))
print(lcm(a, b, gcd(a, b)))
print(lambda_lcm(a, b, gcd(a, b)))
