from brain_games.engine import run_game
from brain_games.games import progression


def main():
    run_game(progression.DESCRIPTION, progression.get_round_data)

