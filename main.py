def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "You cannot divide against 0"


def power(a, b):
    if b != 0:
        return a**b
    else:
        return "You cannot power with 0"


def remainder(a, b):
    return a % b


option = int(input("Select an option to use in the calculator (1/2/3/4/5/6): "))

number_1 = float(input("Please enter the first number: "))
number_2 = float(input("Please enter the second number: "))

if option == "1":
    result = plus(number_1, number_2)
    print(f"The result within {number_1} + {number_2} is: {result}")
elif option == "2":
    result = minus(number_1, number_2)
    print(f"The result within {number_1} - {number_2} is: {result}")
elif option == "3":
    result = multiply(number_1, number_2)
    print(f"The result within {number_1} * {number_2} is: {result}")
elif option == "4":
    result = divide(number_1, number_2)
    print(f"The result within {number_1} / {number_2} is: {result}")
elif option == "5":
    result = power(number_1, number_2)
    print(f"The result within {number_1} ** {number_2} is: {result}")
elif option == "6":
    result = remainder(number_1, number_2)
    print(f"The result within {number_1} % {number_2} is: {result}")
else:
    print("Invalid option")
