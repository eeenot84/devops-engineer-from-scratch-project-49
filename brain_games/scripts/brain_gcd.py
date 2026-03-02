from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    run_game(gcd.DESCRIPTION, gcd.get_round_data)

