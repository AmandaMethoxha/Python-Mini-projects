# Pig Game (CLI)
# Roll a die to build a turn score. Rolling a 1 ends your turn (you bank 0 for the turn).
# First to WIN_SCORE wins.

import random

WIN_SCORE = 50
MIN_PLAYERS = 2
MAX_PLAYERS = 4

def roll_die():
    return random.randint(1, 6)

def ask_players():
    while True:
        players = input(f"Enter the number of players ({MIN_PLAYERS}-{MAX_PLAYERS}): ").strip()
        if players.isdigit():
            n = int(players)
            if MIN_PLAYERS <= n <= MAX_PLAYERS:
                return n
            print(f"Must be between {MIN_PLAYERS}-{MAX_PLAYERS} players.")
        else:
            print("Invalid number, try again.")

def take_turn(player_idx, total_score):
    """Return the points gained this turn for player_idx."""
    print(f"\nPlayer {player_idx + 1}'s turn!")
    print(f"Your total score is: {total_score}\n")
    turn_score = 0
    while True:
        should_roll = input("Roll? (y to roll, anything else to hold): ").strip().lower()
        if should_roll != "y":
            print(f"Holding. Turn total: {turn_score}")
            return turn_score
        value = roll_die()
        print(f"You rolled a {value}.")
        if value == 1:
            print("You rolled a 1! Turn ends, you score 0 this turn.")
            return 0
        turn_score += value
        print(f"Turn score: {turn_score}")

def main():
    print("=== Welcome to Pig (first to 50 wins) ===")
    num_players = ask_players()
    scores = [0] * num_players

    while max(scores) < WIN_SCORE:
        for i in range(num_players):
            gained = take_turn(i, scores[i])
            scores[i] += gained
            print(f"Player {i + 1} total score: {scores[i]}")
            if scores[i] >= WIN_SCORE:
                break

    top_score = max(scores)
    winner = scores.index(top_score) + 1
    print("\n===============================")
    print(f"Player {winner} wins with {top_score} points!")
    print("===============================\n")

if __name__ == "__main__":
    main()
