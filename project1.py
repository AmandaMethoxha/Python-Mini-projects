# PIG GAME
# i build a random  function that generates random numbers with the min value 1 and max6 (dice)
# i enter the number of players which can be decided how we want and in this case is between 1 and 4
# as long as a player says Yes to roll the dice and as long as the number of dice is different than 1 the value add.
# when the number 1 hits the value on that turn equals to 0 and the next player turn comes
# the player that hits first the value 50 wins the game.
import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value) #  Generates a random integer between 1 and 6 (both included)

    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():                      # .isdigit() method checks if the entire string consists of digits (0-9)
        players = int(players)
        if 2 <= players <= 4 :
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid number, try again.")



max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print("\n Player number", player_idx + 1, "turn has just started! \n")
        print("Your total score is:", player_scores[player_idx], "\n")

        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print ("You rolled a 1! Turn Done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)  

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])    

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx +1, 
        "is the winner with a score of:", max_score)