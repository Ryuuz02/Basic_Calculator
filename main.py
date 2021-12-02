def add_nums():
    total = 0
    num_of_nums = int(input("How many numbers would you like to add up\n"))
    for i in range(0, num_of_nums):
        total += float(input("Please type your number below\n"))
    return total


def subtract_nums():
    num_of_nums = int(input("How many numbers would you like to total\n"))
    for i in range(0, num_of_nums):
        if i == 0:
            total = float(input("What is your starting value?"))
        else:
            total -= float(input("What number would you like to subtract it by?\n"))
    return total


def multiply_nums():
    num_of_nums = int(input("How many numbers would you like to multiply\n"))
    for i in range(0, num_of_nums):
        if i == 0:
            total = float(input("Please type your number below\n"))
        else:
            total *= float(input("Please type your number below\n"))
    return total


def divide_nums():
    base_num = float(input("What number would you like to divide"))
    divisor_num = float(input("What would you like to divide it by?"))
    total = base_num / divisor_num
    return total


function_choice = input("Would you like to:"
                        "\n 1: Add multiple numbers"
                        "\n 2: Subtract multiple numbers"
                        "\n 3: Multiply multiple numbers"
                        "\n 4: Divide two numbers\n")
if function_choice == "1":
    print(add_nums())
elif function_choice == "2":
    print(subtract_nums())
elif function_choice == "3":
    print(multiply_nums())
elif function_choice == "4":
    print(divide_nums())
