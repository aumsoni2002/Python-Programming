letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
# PyPassword Generator - Beginner Python Study Notes

## Project Goal

The PyPassword Generator asks the user:

- How many letters they want in a password.
- How many symbols they want.
- How many numbers they want.

Then the program creates a random password using those choices.

There are two challenge levels:

- Easy level: make the password in order, such as letters first, then symbols, then numbers.
- Hard level: make the password in a random order, so letters, symbols, and numbers are mixed together.

---

## Lists

### Simple explanation

A list stores multiple values in one variable.

In this project, the lists hold the possible characters that can be used in the password:

- `letters` stores lowercase and uppercase letters.
- `numbers` stores digit characters.
- `symbols` stores password symbols.

### Why lists are useful

Lists let the program choose from a group of options. Instead of writing every possible letter or number again and again, we keep them in one place and reuse them.

### Code example

```python
letters = ["a", "b", "c"]
numbers = ["1", "2", "3"]
symbols = ["!", "#", "$"]
```

### Line-by-line explanation

- `letters = ["a", "b", "c"]`
  - Creates a list named `letters`.
  - The list contains three strings: `"a"`, `"b"`, and `"c"`.
- `numbers = ["1", "2", "3"]`
  - Creates a list named `numbers`.
  - The numbers are written inside quotes because password characters need to be text.
- `symbols = ["!", "#", "$"]`
  - Creates a list named `symbols`.
  - Each symbol is stored as a separate item.

### Things to remember

- List items are separated by commas.
- Lists use square brackets: `[]`.
- In this project, the numbers are strings, not integers, because they will be joined into a password string later.

---

## Variables

### Simple explanation

A variable is a name that stores a value so you can use it later.

In this project, variables store the user's choices and the password being built.

### Why variables are useful

Variables make programs flexible. If the user asks for 4 letters, the program can remember that number and use it in a loop.

### Code example

```python
nr_letters = 4
password = ""
```

### Line-by-line explanation

- `nr_letters = 4`
  - Stores the number `4` in a variable named `nr_letters`.
  - This could mean the user wants 4 letters in the password.
- `password = ""`
  - Creates a variable named `password`.
  - It starts as an empty string, meaning it has no characters yet.

### Things to remember

- Choose variable names that describe what the value means.
- `password` and `password_list` are different variable names.
- An empty string is written as `""`.

---

## `print()`

### Simple explanation

`print()` shows text or values on the screen.

### Why `print()` is useful

It lets the program communicate with the user. It can welcome the user, show instructions, or display the final password.

### Code example

```python
print("Welcome to the PyPassword Generator!")
```

### Line-by-line explanation

- `print(...)`
  - Runs Python's built-in print function.
- `"Welcome to the PyPassword Generator!"`
  - This is the text that appears on the screen.

### Things to remember

- Text must be inside quotes.
- `print(password)` prints the value stored in the variable.
- `print("password")` prints the word password, not the variable's value.

---

## `input()`

### Simple explanation

`input()` asks the user to type something.

Python waits until the user enters an answer.

### Why `input()` is useful

It makes the program interactive. The password generator can create different passwords depending on what the user types.

### Code example

```python
answer = input("How many letters would you like?\n")
```

### Line-by-line explanation

- `input("How many letters would you like?\n")`
  - Shows the question to the user.
  - `\n` moves the cursor to the next line.
- `answer = ...`
  - Stores the user's typed answer in the variable `answer`.

### Things to remember

- `input()` always gives back a string.
- If the user types `4`, Python receives it as `"4"`, not as the number `4`.

---

## `int()`

### Simple explanation

`int()` converts a value into a whole number.

### Why `int()` is useful

The user's answer from `input()` is text, but `range()` needs a number. `int()` changes the user's answer into a number Python can count with.

### Code example

```python
nr_letters = int(input("How many letters would you like?\n"))
```

### Line-by-line explanation

- `input("How many letters would you like?\n")`
  - Gets the user's answer as text.
- `int(...)`
  - Converts that text into a whole number.
- `nr_letters = ...`
  - Stores the whole number in `nr_letters`.

### Things to remember

- `int("4")` becomes `4`.
- `int("hello")` causes an error because `"hello"` cannot become a number.
- This project assumes the user types valid numbers.

---

## The `random` Module

### Simple explanation

A module is extra code that Python can import and use.

The `random` module helps Python make random choices.

### Why the `random` module is useful

Passwords should not be predictable. Random choices make each generated password different.

### Code example

```python
import random

letter = random.choice(["a", "b", "c"])
print(letter)
```

### Line-by-line explanation

- `import random`
  - Gives the program access to Python's random tools.
- `letter = random.choice(["a", "b", "c"])`
  - Chooses one random item from the list.
  - Stores that item in `letter`.
- `print(letter)`
  - Displays the randomly chosen letter.

### Things to remember

- You must `import random` before using `random.choice()` or `random.shuffle()`.
- Random means the result can be different each time the program runs.

---

## `random.choice()`

### Simple explanation

`random.choice()` picks one random item from a sequence, such as a list.

### Why `random.choice()` is useful

It lets the password generator pick a random letter, symbol, or number without you choosing the position manually.

### Code example

```python
import random

letters = ["a", "b", "c"]
random_letter = random.choice(letters)
print(random_letter)
```

### Line-by-line explanation

- `import random`
  - Loads the random module.
- `letters = ["a", "b", "c"]`
  - Creates a list of possible letters.
- `random_letter = random.choice(letters)`
  - Picks one item from `letters`.
  - Stores it in `random_letter`.
- `print(random_letter)`
  - Shows the random letter.

### Things to remember

- `random.choice(letters)` chooses from the values inside the list.
- Do not write `random.choice()` with nothing inside the parentheses.

---

## `for` Loops

### Simple explanation

A `for` loop repeats code.

In this project, loops repeat the process of adding letters, symbols, and numbers to the password.

### Why `for` loops are useful

If the user wants 14 letters, you do not want to write the same line 14 times. A loop can repeat it automatically.

### Code example

```python
for char in range(0, 4):
    print("Add one letter")
```

### Line-by-line explanation

- `for char in range(0, 4):`
  - Starts a loop.
  - The loop runs once for each number in the range.
  - `range(0, 4)` gives 0, 1, 2, and 3, so the loop runs 4 times.
- `print("Add one letter")`
  - This indented line runs each time the loop repeats.

### Things to remember

- The colon `:` starts the loop block.
- The code inside the loop must be indented.
- The variable name `char` is just a placeholder here. The project does not need its actual value.

---

## `range()`

### Simple explanation

`range()` creates a sequence of numbers that a loop can count through.

### Why `range()` is useful

It lets the program repeat an action a specific number of times.

### Code example

```python
for number in range(0, 4):
    print(number)
```

### Line-by-line explanation

- `range(0, 4)`
  - Starts at `0`.
  - Stops before `4`.
  - Produces `0`, `1`, `2`, and `3`.
- `for number in range(0, 4):`
  - Runs the loop once for each number.
- `print(number)`
  - Prints the current number each time.

### Things to remember

- The stop number is not included.
- `range(0, 4)` runs 4 times.
- `range(1, 4)` runs only 3 times: 1, 2, and 3.
- To repeat something `nr_letters` times, `range(0, nr_letters)` is clean and simple.

---

## Building a String with Concatenation

### Simple explanation

String concatenation means joining strings together.

In the easy version, the password starts as an empty string, and each random character is added to the end.

### Why string concatenation is useful

It lets the program build a longer password one character at a time.

### Code example

```python
password = ""
password += "A"
password += "7"
print(password)
```

### Line-by-line explanation

- `password = ""`
  - Starts with an empty password.
- `password += "A"`
  - Adds `"A"` to the end of the password.
  - This is the shorter version of `password = password + "A"`.
- `password += "7"`
  - Adds `"7"` after `"A"`.
- `print(password)`
  - Prints `A7`.

### Things to remember

- You can only concatenate strings with other strings.
- This is why the `numbers` list stores `"7"` as a string, not `7` as an integer.
- `+=` updates the old value by adding something to it.

---

## Easy Level Password Logic

### Simple explanation

The easy version creates the password in a fixed order:

1. Add all the letters.
2. Add all the symbols.
3. Add all the numbers.

### Why this is useful

It is a simpler first step. It helps you practice loops, random choices, and string building before solving the harder random-order version.

### Code example

```python
import random

letters = ["a", "b", "c"]
symbols = ["!", "#"]
numbers = ["1", "2"]

password = ""

for char in range(0, 2):
    password += random.choice(letters)

for char in range(0, 1):
    password += random.choice(symbols)

for char in range(0, 1):
    password += random.choice(numbers)

print(password)
```

### Line-by-line explanation

- `import random`
  - Loads the random module.
- `letters`, `symbols`, and `numbers`
  - Store the possible password characters.
- `password = ""`
  - Starts the password as an empty string.
- `for char in range(0, 2):`
  - Repeats the next indented line 2 times.
- `password += random.choice(letters)`
  - Picks a random letter and adds it to the password.
- `for char in range(0, 1):`
  - Repeats the next line 1 time.
- `password += random.choice(symbols)`
  - Adds one random symbol.
- `password += random.choice(numbers)`
  - Adds one random number character.
- `print(password)`
  - Shows the final password.

### Things to remember

- The easy version works, but the order is predictable.
- If a password always ends with numbers, it may be easier to guess than a fully shuffled password.

---

## Lists and `.append()`

### Simple explanation

`.append()` adds one new item to the end of a list.

In the hard version, the password characters are first stored in a list so they can be shuffled.

### Why `.append()` is useful

Lists are easy to rearrange. By appending characters to a list first, we can shuffle them before turning them into the final password.

### Code example

```python
password_list = []
password_list.append("A")
password_list.append("7")
print(password_list)
```

### Line-by-line explanation

- `password_list = []`
  - Creates an empty list.
- `password_list.append("A")`
  - Adds `"A"` to the list.
- `password_list.append("7")`
  - Adds `"7"` after `"A"`.
- `print(password_list)`
  - Prints `["A", "7"]`.

### Things to remember

- `.append()` changes the existing list.
- `.append()` adds one item at a time.
- A list of characters is not the same thing as a password string yet.

---

## `random.shuffle()`

### Simple explanation

`random.shuffle()` changes the order of items in a list.

### Why `random.shuffle()` is useful

It makes the hard-level password stronger by mixing letters, symbols, and numbers into a random order.

### Code example

```python
import random

password_list = ["A", "b", "!", "3"]
random.shuffle(password_list)
print(password_list)
```

### Line-by-line explanation

- `import random`
  - Loads the random module.
- `password_list = ["A", "b", "!", "3"]`
  - Creates a list of password characters.
- `random.shuffle(password_list)`
  - Rearranges the items inside `password_list`.
- `print(password_list)`
  - Shows the shuffled list.

### Things to remember

- `random.shuffle()` works on lists.
- It changes the list directly.
- It does not create a new string password by itself.

---

## Turning a List Back Into a String

### Simple explanation

After shuffling, the password characters are still in a list. To display a normal password, we need to join them into one string.

### Why this is useful

Users expect a password like `aB3!`, not a list like `["a", "B", "3", "!"]`.

### Code example

```python
password_list = ["a", "B", "3", "!"]
password = ""

for char in password_list:
    password += char

print(password)
```

### Line-by-line explanation

- `password_list = ["a", "B", "3", "!"]`
  - Stores each password character as a list item.
- `password = ""`
  - Starts an empty string for the final password.
- `for char in password_list:`
  - Loops through each character in the list.
- `password += char`
  - Adds the current character to the password string.
- `print(password)`
  - Prints `aB3!`.

### Things to remember

- The loop visits each item in order.
- After `random.shuffle()`, the order is already mixed.
- The final password should be a string.

---

## f-Strings

### Simple explanation

An f-string lets you put a variable inside a string.

### Why f-strings are useful

They make output easier to read and write.

### Code example

```python
password = "aB3!"
print(f"Your password is: {password}")
```

### Line-by-line explanation

- `password = "aB3!"`
  - Stores a password string.
- `print(f"Your password is: {password}")`
  - The `f` tells Python this is an f-string.
  - `{password}` is replaced with the value stored in the `password` variable.

### Things to remember

- Put `f` before the opening quote.
- Put variable names inside curly braces: `{}`.
- Without the `f`, Python prints `{password}` as plain text.

---

## Hard Level Password Logic

### Simple explanation

The hard version creates a list of random password characters, shuffles the list, and then turns it into a string.

### Why this is useful

The password is harder to guess because the letters, symbols, and numbers are not always in the same positions.

### Code example

```python
import random

letters = ["a", "b", "c"]
symbols = ["!", "#"]
numbers = ["1", "2"]

password_list = []

for char in range(0, 2):
    password_list.append(random.choice(letters))

for char in range(0, 1):
    password_list.append(random.choice(symbols))

for char in range(0, 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
```

### Line-by-line explanation

- `import random`
  - Loads the tools for random choices and shuffling.
- `letters`, `symbols`, and `numbers`
  - Store the possible characters.
- `password_list = []`
  - Creates an empty list for the password characters.
- First `for` loop
  - Adds 2 random letters to `password_list`.
- Second `for` loop
  - Adds 1 random symbol to `password_list`.
- Third `for` loop
  - Adds 1 random number character to `password_list`.
- `random.shuffle(password_list)`
  - Mixes the order of all characters in the list.
- `password = ""`
  - Creates an empty string for the final password.
- `for char in password_list:`
  - Goes through the shuffled list one item at a time.
- `password += char`
  - Adds each character to the password string.
- `print(f"Your password is: {password}")`
  - Displays the final password.

### Things to remember

- Build the list first.
- Shuffle the list before making the final string.
- Print the final string, not just the list.

---

## Easy Level vs. Hard Level

### Easy level

Example result:

```python
abcd!#12
```

The order is predictable:

- Letters first.
- Symbols next.
- Numbers last.

### Hard level

Example result:

```python
a!1b#c2d
```

The order is mixed:

- Letters, symbols, and numbers can appear anywhere.
- The password is less predictable.

### Why the hard level is better

If someone knows that the last characters are always numbers, they have less to guess. Random order gives fewer clues about the password pattern.

---

## Common Mistakes to Watch For

- Forgetting `import random`
  - `random.choice()` and `random.shuffle()` will not work unless the random module is imported.

- Forgetting to convert input with `int()`
  - `range()` needs a number, not a string.

- Misunderstanding `range()`
  - `range(0, 4)` runs 4 times.
  - `range(1, 4)` runs only 3 times.

- Trying to shuffle a string
  - `random.shuffle()` works on a list, not directly on a string.

- Printing the list instead of the final password
  - `["a", "B", "3", "!"]` is useful for debugging.
  - `aB3!` is the password the user wants.

- Forgetting indentation
  - The code inside a loop must be indented.

---

## Big Picture Summary

The PyPassword Generator practices several important beginner Python skills:

- Lists store possible password characters.
- `input()` asks the user what they want.
- `int()` converts typed text into numbers.
- `for` loops repeat code.
- `range()` controls how many times a loop runs.
- `random.choice()` picks random characters.
- String concatenation builds a password one character at a time.
- `.append()` adds characters to a list.
- `random.shuffle()` mixes the list order.
- f-strings make the final message easy to print.

The easy version helps you understand the basic steps. The hard version improves the password by making the order random.
"""
