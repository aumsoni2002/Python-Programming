# Python Programming

I am learning Python and using this repository to document my progress. It
contains exercises and projects from Day 1 through Day 26.

## What I have learned so far

- Variables, data types, strings, and mathematical operations
- User input, type conversion, and number manipulation
- Conditional statements and logical operators
- Lists, dictionaries, and nested data structures
- `for` and `while` loops
- Functions, parameters, return values, and scope
- Debugging and problem-solving techniques
- Randomization and working with Python modules
- Object-oriented programming with classes and objects
- Event listeners and graphical programs using Turtle
- Breaking larger programs into multiple Python files
- Reading, writing, and appending text files
- Relative paths, absolute paths, and `pathlib`
- Saving data between program runs
- Reading and writing CSV files with Python's `csv` module and pandas
- Working with pandas DataFrames and Series
- Selecting columns, filtering rows, and analysing tabular data
- Creating and filtering lists with list comprehensions
- Creating and filtering dictionaries with dictionary comprehensions
- Looping through pandas DataFrame rows with `iterrows()`
- Converting words into NATO phonetic alphabet code words

## Featured projects

### NATO Phonetic Alphabet - Day 26

A command-line program that reads the NATO phonetic alphabet from a CSV file,
creates a lookup dictionary with a dictionary comprehension, and converts a
word entered by the user into its phonetic code words.

Navigate to [`Day 26/NATO-alphabet`](Day%2026/NATO-alphabet/) to see the
project.

### U.S. States Game - Day 25

An interactive Turtle-based geography game where the player names U.S. states
and correct answers are written at their map coordinates. When the game ends,
the states that still need practice are saved to a CSV file.

Navigate to [`Day 25/us-states-game`](Day%2025/us-states-game/) to see the
project.

### Mail Merge Project - Day 24

A file-handling project that reads a list of names and a letter template,
replaces the name placeholder, and saves a personalized letter for every
recipient.

Navigate to [`Day 24/Mail Merge Project`](Day%2024/Mail%20Merge%20Project/) to
see the project.

### Turtle Crossing Game - Day 23

A Turtle-based road-crossing game where the player avoids moving cars and
tries to reach the other side. Each successful crossing increases the level
and makes the cars move faster.

Navigate to [`Day 23`](Day%2023/) to see the project.

### Pong Game - Day 22

A two-player Pong game built with Turtle. It includes paddle controls, ball
movement, collision detection, scoring, and gradually increasing ball speed.

Navigate to [`Day 22`](Day%2022/) to see the project.

### Snake Game - Days 20 and 21

The classic Snake game, organized into separate classes for the snake, food,
and scoreboard. It now saves the high score between program runs and resets
the game after a collision so the player can keep trying.

Navigate to [`Day 20_21`](Day%2020_21/) to see the project.

### Quiz Game - Day 17

An object-oriented quiz application that stores questions as objects, checks
the player's answers, and keeps track of the score.

Navigate to [`Day 17/quiz-game-start`](Day%2017/quiz-game-start/) to see the
project.

### Coffee Machine - Days 15 and 16

A coffee-machine simulation that handles drink selection, resources, payments,
and change. Day 16 rebuilds the program using object-oriented programming.

Navigate to [`Day 15/Coffee Machine Project`](Day%2015/Coffee%20Machine%20Project/)
or [`Day 16/oop-coffee-machine-start`](Day%2016/oop-coffee-machine-start/).

### Higher or Lower - Day 14

A comparison game where the player guesses which public figure has more
followers while trying to build a winning streak.

Navigate to [`Day 14/Higher or Lower Project`](Day%2014/Higher%20or%20Lower%20Project/).

### Blackjack - Day 11

A command-line version of Blackjack featuring card dealing, score calculation,
computer turns, and win-or-lose decisions.

Navigate to [`Day 11/task`](Day%2011/task/) to see the project.

### Other projects

The earlier folders contain projects such as a calculator, blind auction,
Caesar cipher, Hangman, password generator, rock-paper-scissors, treasure
island, and a tip calculator. Browse the [`Day 1`](Day%201/) through
[`Day 26`](Day%2026/) folders to follow my progress.

## pandas dependency

Days 25 and 26 use pandas for CSV data analysis and DataFrame exercises.
Install it from the repository root with:

```bash
python -m pip install -r "Day 25/requirements.txt"
```
