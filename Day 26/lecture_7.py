# Dictionary Comprehension
import random

# Create Dictionary from a list:
#   new_dict = {new_key:new_value for item in list}


# Create Dictionary from a Dictionary:
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)


passed_students = {student: score for (student, score) in student_scores.items() if score > 59}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split()
result = {word: len(word) for word in list_of_words}
print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp_c* 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)