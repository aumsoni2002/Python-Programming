from pathlib import Path
from turtle import Screen, Turtle

import pandas as pd


# `__file__` is the path of this Python file. Starting from that location makes
# these file paths reliable. In the old version, paths such as "./50_states.csv"
# depended on the folder from which the program was started. That could cause a
# FileNotFoundError when the game was launched from the repository root.
PROJECT_FOLDER = Path(__file__).resolve().parent
MAP_FILE = PROJECT_FOLDER / "blank_states_img.gif"
STATE_DATA_FILE = PROJECT_FOLDER / "50_states.csv"
STATES_TO_LEARN_FILE = PROJECT_FOLDER / "states_to_learn.csv"


def save_states_to_learn(all_states, correct_answers):
    """Save the states that were not guessed without an index column."""
    # This list comprehension checks every real state. It keeps only the states
    # that are missing from `correct_answers`. Your old code used a separate
    # empty list and a for loop. Both approaches work; this is a shorter way to
    # build the same list.
    states_to_learn = [
        state for state in all_states if state not in correct_answers
    ]

    # Giving pandas a dictionary creates a clear column heading named "state".
    # `index=False` stops pandas from adding an extra 0, 1, 2... column to the
    # CSV. That extra index was included by the old `to_csv()` call.
    pd.DataFrame({"state": states_to_learn}).to_csv(
        STATES_TO_LEARN_FILE, index=False
    )


def play_game():
    """Run the interactive U.S. states guessing game."""
    data = pd.read_csv(STATE_DATA_FILE)

    # We only need the names when checking answers, so this creates a simple
    # list such as ["Alabama", "Alaska", ...]. The old `data.values.tolist()`
    # also included the x and y coordinates in every item.
    all_states = data["state"].to_list()
    correct_answers = []

    screen = Screen()
    screen.title("U.S. States Game")
    screen.addshape(str(MAP_FILE))

    map_turtle = Turtle()
    map_turtle.shape(str(MAP_FILE))

    state_writer = Turtle()
    state_writer.penup()
    state_writer.hideturtle()

    # The number of correct answers is also the score, so a separate `score`
    # variable is not needed. Comparing against `len(all_states)` also avoids
    # writing the number 50 in the loop condition.
    while len(correct_answers) < len(all_states):
        user_answer = screen.textinput(
            title=f"{len(correct_answers)}/50 States Correct",
            prompt="What's another state name? (q to quit)",
        )

        # Clicking Cancel or closing the input dialog gives us `None`, not text.
        # We must check for None before using string methods such as `.lower()`.
        # Otherwise the program crashes with an AttributeError. `break` exits
        # the loop immediately, so the letter q is not processed as an answer.
        if user_answer is None or user_answer.strip().lower() == "q":
            break

        # `strip()` removes accidental spaces before or after the answer.
        # `title()` changes input such as "new york" into "New York" so it
        # matches the capitalization used in the CSV file.
        state_name = user_answer.strip().title()

        # The second condition is important: it prevents the same correct state
        # from being counted more than once. Previously, repeatedly entering a
        # state such as Alabama increased the score every time.
        if state_name in all_states and state_name not in correct_answers:
            # Filtering finds the one DataFrame row for this state. `.iloc[0]`
            # takes that row, which lets us reuse it for the name's x and y
            # coordinates instead of filtering the DataFrame three times.
            state_row = data[data["state"] == state_name].iloc[0]
            state_writer.goto((int(state_row["x"]), int(state_row["y"])))
            state_writer.write(state_name)
            correct_answers.append(state_name)

    # Reaching this point can mean either that the player quit or that every
    # state was guessed. We only show the winning message in the second case.
    if len(correct_answers) == len(all_states):
        state_writer.goto((0, 0))
        state_writer.write("You guessed all of them!", align="center")

    save_states_to_learn(all_states, correct_answers)

    # Keep the completed map open until the player clicks it. Without this, the
    # Turtle window may close as soon as the Python program reaches its end.
    screen.exitonclick()


# This check runs the game only when this file is started directly. It does not
# run `play_game()` when the file is imported for testing or reused elsewhere.
if __name__ == "__main__":
    play_game()
