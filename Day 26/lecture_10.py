student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print("--------------")
    print(index) # this prints the index number of each row
    print(row) # this prints all the information of that row
    print(row.student) # this prints all the students
    print(row.score) # this prints all the scores

# Create Dictionary from a data frame with a comprehension
# new_dict = {new_key: new_value for (index, row) in df.iterrows()}