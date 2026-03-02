import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )
    return first_number


def get_round_data():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f"{first_number} {second_number}"
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer

