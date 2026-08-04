# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

more_bidders = "yes"
total_bidders = {}

print(logo)

while more_bidders == "yes":
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    total_bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'")

    print("\n" * 20)

winner_key = ""
winner_value = 0

for key in total_bidders:
    if total_bidders[key] > winner_value:
        winner_key = key
        winner_value = total_bidders[key]

print(f"The winner is {winner_key} with a bid of ${winner_value}")