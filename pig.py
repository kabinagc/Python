import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid , Try Again ")

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:

    for player_index in range(players):
        print("\n Player", player_index + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("your score is :", current_score)

        player_scores[player_index] += current_score
    print("Your total score is:", player_scores[player_index])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score) + 1  # Add 1 to get the player number
print("Player number", winning_idx, "is the winner with a score of:", max_score)

        







