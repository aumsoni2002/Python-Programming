# HIGHEST SCORE NOTES
#
# This lesson uses for loops with lists of numbers.
#
# Main ideas:
# - Python has built-in number functions like sum() and max().
# - We can also recreate similar logic ourselves using loops.
# - A loop can go through each score one by one.
# - A variable can remember a running total or current highest value.


# This list stores many student exam scores.
# Each item in the list is an integer.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


# 1. USING sum()
#
# sum() is a built-in Python function.
# It adds all the numbers inside a list.
#
# The list is passed into the parentheses.

total_exam_score = sum(student_scores)
print(total_exam_score)


# 2. MANUALLY ADDING SCORES WITH A FOR LOOP
#
# We can build the same idea ourselves.
#
# First, create a variable to hold the running total.
# It starts at 0 because we have not added any scores yet.

manual_sum = 0

# This loop goes through each score in student_scores.
# Each time the loop runs, score becomes the next number in the list.
for score in student_scores:
    # += means "add this value to the current value".
    #
    # manual_sum += score
    #
    # means the same as:
    #
    # manual_sum = manual_sum + score
    #
    # Each score gets added to the running total.
    manual_sum += score

# This should print the same result as sum(student_scores).
print(manual_sum)


# 3. USING max()
#
# max() is another built-in Python function.
# It finds the largest value inside a list.

built_in_highest_score = max(student_scores)
print(built_in_highest_score)


# 4. MANUALLY FINDING THE HIGHEST SCORE
#
# The challenge is to recreate max() ourselves using:
# - a for loop
# - a variable
# - an if statement
#
# We need a variable to remember the highest score seen so far.
#
# A safe way to start is to use the first score in the list.
# That means max_score starts as 150.
#
# This is safer than starting at 0 if a list could contain negative numbers.
max_score = student_scores[0]


# This loop checks every score in the list one by one.
for score in student_scores:
    # This condition asks:
    # Is the current score greater than the highest score we have seen so far?
    #
    # If yes, then we found a new highest score.
    if score > max_score:
        # This updates max_score to the new highest value.
        #
        # Example:
        # At the start, max_score is 150.
        # If score is 185, then 185 > 150 is True.
        # So max_score becomes 185.
        #
        # Later, if score is 199, then 199 > 185 is True.
        # So max_score becomes 199.
        max_score = score


# This print is outside the for loop because it is not indented.
# That means it only runs once, after the loop has checked every score.
#
# If this print was indented inside the loop,
# it would print the current max_score many times while the loop is still running.
print(max_score)


# STEP-BY-STEP EXAMPLE
#
# Imagine the first few scores are:
# [150, 142, 185]
#
# Start:
# max_score = 150
#
# First loop:
# score = 150
# Is 150 > 150? No.
# max_score stays 150.
#
# Second loop:
# score = 142
# Is 142 > 150? No.
# max_score stays 150.
#
# Third loop:
# score = 185
# Is 185 > 150? Yes.
# max_score becomes 185.
#
# The loop keeps going until every score has been checked.


# QUICK REVIEW
#
# sum(student_scores)
# Adds every score in the list.
#
# max(student_scores)
# Finds the highest score in the list.
#
# for score in student_scores:
# Goes through each score one at a time.
#
# manual_sum += score
# Adds the current score to the running total.
#
# if score > max_score:
# Checks whether the current score is higher than the highest score so far.
#
# max_score = score
# Updates the highest score when a bigger one is found.
