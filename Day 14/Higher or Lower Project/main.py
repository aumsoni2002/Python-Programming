from art import logo, vs
from game_data import data
import random

def generate_players(player_a, player_b):
    is_data_empty = False
    if len(data) == 2:
        is_data_empty = True
        return player_a, player_b, is_data_empty

    for player in data:
        if player == player_a:
           data.remove(player)

    player_a = player_b
    is_unique = True
    while is_unique:
        player_b = random.choice(data)
        if player_a != player_b:
            is_unique = False

    return player_a, player_b, is_data_empty

def score_counter(current_score, player_chose, player_a, player_b):
    if player_chose == "a":
        if player_a["follower_count"] > player_b["follower_count"]:
            return current_score + 1, True
        else:
            return current_score, False
    else:
        if player_b["follower_count"] > player_a["follower_count"]:
            return current_score + 1, True
        else:
            return current_score, False

total_score = 0
is_guess_correct = True

print(logo)
player_1, player_2 = random.sample(data, 2)
while is_guess_correct:
    print(f"\nYour Current Score is: {total_score}")
    print(f"Compare A: {player_1["name"]}, a {player_1["description"]}, from {player_1["country"]}")
    print(vs)
    print(f"Compare B: {player_2["name"]}, a {player_2["description"]}, from {player_2["country"]}\n")

    player_choice = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    total_score, is_guess_correct = score_counter(total_score, player_choice, player_1, player_2)
    player_1, player_2, data_empty = generate_players(player_1, player_2)

    if data_empty:
        print("You have reached the end of the List!!")
        break


print(f"Your Score is: {total_score}")