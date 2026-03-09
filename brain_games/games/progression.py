import random

DESCRIPTION = "What number is missing in the progression?"

MIN_LENGTH = 5
MAX_LENGTH = 10

MIN_START = 1
MAX_START = 50

MIN_STEP = 1
MAX_STEP = 10


def get_round_data():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    stop = start + step * length
    progression = list(range(start, stop, step))

    hidden_index = random.randrange(length)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer

