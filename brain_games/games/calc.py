import random

DESCRIPTION = "What is the result of the expression?"

OPERATORS = ("+", "-", "*")

MIN_NUMBER = 1
MAX_NUMBER = 25


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
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    question = f"{first_number} {operator} {second_number}"
    correct_answer = str(calculate(first_number, operator, second_number))
    return question, correct_answer

