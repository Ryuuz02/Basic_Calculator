# Function for adding a potentially infinite amount of numbers
def add_nums():
    total = 0
    num_of_nums = int(input("How many numbers would you like to add up\n"))
    for i in range(0, num_of_nums):
        total += float(input("Please type your number below\n"))
    return total


def evaluate_expression(num1, exp, num2):
    if exp == "x" or exp == "*":
        return num1 * num2
    elif exp == "+":
        return num1 + num2
    elif exp == "-":
        return num1 - num2
    elif exp == "/":
        return num1 / num2
    elif exp == "^":
        return num1 ** num2


# Function to subtract infinite amount of numbers
def subtract_nums():
    total = 0
    num_of_nums = int(input("How many numbers would you like to total\n"))
    for i in range(0, num_of_nums):
        if i == 0:
            total = float(input("What is your starting value?\n"))
        else:
            total -= float(input("What number would you like to subtract it by?\n"))
    return total


# Function to multiply any amount of numbers
def multiply_nums():
    total = 0
    num_of_nums = int(input("How many numbers would you like to multiply\n"))
    for i in range(0, num_of_nums):
        if i == 0:
            total = float(input("Please type your number below\n"))
        else:
            total *= float(input("Please type your number below\n"))
    return total


# Function to divide two user inputed numbers
def divide_nums():
    base_num = float(input("What number would you like to divide\n"))
    divisor_num = float(input("What would you like to divide it by?\n"))
    return base_num / divisor_num


def evaluate_equation(equation_input):
    equation_split = equation_input.split()
    function_index_list = []
    function_lst = []
    for i in range(0, len(equation_split)):
        if equation_split[i] in math_functions:
            function_index_list.append(i)
            function_lst.append(equation_split[i])
    while "^" in function_lst:
        for i in range(0, len(function_lst)):
            if equation_split[function_index_list[i]] == "^":
                value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "^",
                                            int(equation_split[function_index_list[i] + 1]))
                equation_split[function_index_list[i]] = value
                equation_split.pop(function_index_list[i] + 1)
                equation_split.pop(function_index_list[i] - 1)
                function_lst.remove("^")
                for j in range(0, len(function_index_list)):
                    if function_index_list[j] > function_index_list[i]:
                        function_index_list[j] -= 2
    while "*" in function_lst or "x" in function_lst:
        for i in range(0, len(function_lst)):
            if equation_split[function_index_list[i]] == "*":
                value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "*",
                                            int(equation_split[function_index_list[i] + 1]))
                equation_split[function_index_list[i]] = value
                equation_split.pop(function_index_list[i] + 1)
                equation_split.pop(function_index_list[i] - 1)
                function_lst.remove("*")
                for j in range(0, len(function_index_list)):
                    if function_index_list[j] > function_index_list[i]:
                        function_index_list[j] -= 2
    while "/" in function_lst:
        for i in range(0, len(function_lst)):
            if equation_split[function_index_list[i]] == "/":
                value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "/",
                                            int(equation_split[function_index_list[i] + 1]))
                equation_split[function_index_list[i]] = value
                equation_split.pop(function_index_list[i] + 1)
                equation_split.pop(function_index_list[i] - 1)
                function_lst.remove("/")
                for j in range(0, len(function_index_list)):
                    if function_index_list[j] > function_index_list[i]:
                        function_index_list[j] -= 2
    while "+" in function_lst:
        for i in range(0, len(function_lst)):
            if equation_split[function_index_list[i]] == "+":
                value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "+",
                                            int(equation_split[function_index_list[i] + 1]))
                equation_split[function_index_list[i]] = value
                equation_split.pop(function_index_list[i] + 1)
                equation_split.pop(function_index_list[i] - 1)
                function_lst.remove("+")
                for j in range(0, len(function_index_list)):
                    if function_index_list[j] > function_index_list[i]:
                        function_index_list[j] -= 2
    while "-" in function_lst:
        for i in range(0, len(function_lst)):
            if equation_split[function_index_list[i]] == "-":
                value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "-",
                                            int(equation_split[function_index_list[i] + 1]))
                equation_split[function_index_list[i]] = value
                equation_split.pop(function_index_list[i] + 1)
                equation_split.pop(function_index_list[i] - 1)
                function_lst.remove("-")
                for j in range(0, len(function_index_list)):
                    if function_index_list[j] > function_index_list[i]:
                        function_index_list[j] -= 2



        """if equation_split[function_index_list[i]] == "(":
            parenthesis_range = [function_index_list[i]]
            for j in range(0, len(function_index_list)):
                if equation_split[function_index_list[j]] == ")":
                    parenthesis_range.append(function_index_list[j])
                    j = len(function_index_list) - 1
            parenthesis_equation = equation_split[parenthesis_range[0] + 1:parenthesis_range[1]]
            parenthesis_value = evaluate_equation(parenthesis_equation)
        if equation_split[function_index_list[i]] == "^":
            value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "^",
                                        int(equation_split[function_index_list[i] + 1]))
            equation_split[function_index_list[i]] = value
            equation_split.pop(function_index_list[i] + 1)
            equation_split.pop(function_index_list[i] - 1)
            for j in range(0, len(function_index_list)):
                if function_index_list[j] > function_index_list[i]:
                    function_index_list[j] -= 2
            if len(equation_split) == 1:
                break
        elif equation_split[function_index_list[i]] == "*" or equation_split[function_index_list[i]] == "x":
            value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "*",
                                        int(equation_split[function_index_list[i] + 1]))
            equation_split[function_index_list[i]] = value
            equation_split.pop(function_index_list[i] + 1)
            equation_split.pop(function_index_list[i] - 1)
            for j in range(0, len(function_index_list)):
                if function_index_list[j] > function_index_list[i]:
                    function_index_list[j] -= 2
            if len(equation_split) == 1:
                break
        elif equation_split[function_index_list[i]] == "/":
            value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "/",
                                        int(equation_split[function_index_list[i] + 1]))
            equation_split[function_index_list[i]] = value
            equation_split.pop(function_index_list[i] + 1)
            equation_split.pop(function_index_list[i] - 1)
            for j in range(0, len(function_index_list)):
                if function_index_list[j] > function_index_list[i]:
                    function_index_list[j] -= 2
            if len(equation_split) == 1:
                break
        elif equation_split[function_index_list[i]] == "+":
            value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "+",
                                        int(equation_split[function_index_list[i] + 1]))
            equation_split[function_index_list[i]] = value
            equation_split.pop(function_index_list[i] + 1)
            equation_split.pop(function_index_list[i] - 1)
            for j in range(0, len(function_index_list)):
                if function_index_list[j] > function_index_list[i]:
                    function_index_list[j] -= 2
            if len(equation_split) == 1:
                break
        elif equation_split[function_index_list[i]] == "-":
            value = evaluate_expression(int(equation_split[function_index_list[i] - 1]), "-",
                                        int(equation_split[function_index_list[i] + 1]))
            equation_split[function_index_list[i]] = value
            equation_split.pop(function_index_list[i] + 1)
            equation_split.pop(function_index_list[i] - 1)
            for j in range(0, len(function_index_list)):
                if function_index_list[j] > function_index_list[i]:
                    function_index_list[j] -= 2
            if len(equation_split) == 1:
                break"""

    print(equation_split)


math_functions = ["x", "*", "-", "+", "/", "^", "(", ")"]

function_choice = input("Would you like to:"
                        "\n 1: Add multiple numbers"
                        "\n 2: Subtract multiple numbers"
                        "\n 3: Multiply multiple numbers"
                        "\n 4: Divide two numbers"
                        "\n 5: Input an entire equation\n")
if function_choice == "1":
    print(add_nums())
elif function_choice == "2":
    print(subtract_nums())
elif function_choice == "3":
    print(multiply_nums())
elif function_choice == "4":
    print(divide_nums())
elif function_choice == "5":
    evaluate_equation(input("Please type out your equation (This is a WIP, so currently it can only do -, +, x"
                            ", *, /, and ^ operations. Also you must put a space in between, for example '4 + 5')\n"))
