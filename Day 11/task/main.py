import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def compute_player_total(player_cards):
    player_total = 0
    for card in player_cards:
        player_total = player_total + card

    if player_total > 21 and 11 in player_cards:
        player_total = player_total - 10
        index_of_11 = player_cards.index(11)
        player_cards[index_of_11] = 1

    return player_total


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play_game == 'y':
    print(logo)
    your_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    y_total = compute_player_total(your_cards)
    c_total = compute_player_total(computer_cards)

    print(f"Your cards: {your_cards}, current score: {y_total}")
    print(f"Computer's first card: {computer_cards[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == 'y':
        your_cards.append(random.choice(cards))
        y_total = compute_player_total(your_cards)
        if y_total < 21:
            print(f"Your cards: {your_cards}, current score: {y_total}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            break

    if y_total > 21:
        print(f"Your final cards: {your_cards}, final score: {y_total}")
        print(f"Computer's final hand: {computer_cards[0]}, final score: {computer_cards[0]}")
        print("You went over. You lose.")
    else:
        while c_total < 17:
            computer_cards.append(random.choice(cards))
            c_total = compute_player_total(computer_cards)

        print(f"Your final cards: {your_cards}, final score: {y_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {c_total}")
        if y_total == 21 or c_total > 21 or y_total > c_total:
            print("You win.")
        elif y_total < c_total:
            print("You lose.")
        else:
            print("It's a draw")

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print("\n" * 20)