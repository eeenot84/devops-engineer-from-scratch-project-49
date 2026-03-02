import random

DESCRIPTION = "Find the greatest common divisor of given numbers."

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )
    return first_number


def get_round_data():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{first_number} {second_number}"
    correct_answer = str(gcd(first_number, second_number))
    return question, correct_answer

