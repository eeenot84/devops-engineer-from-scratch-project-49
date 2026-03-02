import random

DESCRIPTION = "What is the result of the expression?"

OPERATORS = ("+", "-", "*")


def calculate(first_number, operator, second_number):
    match operator:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case _:
            raise ValueError(f"Unknown operator: {operator}")


def get_round_data():
    first_number = random.randint(1, 25)
    second_number = random.randint(1, 25)
    operator = random.choice(OPERATORS)
    question = f"{first_number} {operator} {second_number}"
    correct_answer = str(calculate(first_number, operator, second_number))
    return question, correct_answer

