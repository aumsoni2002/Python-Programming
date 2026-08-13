# List Comprehension:
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]

numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)


name = "Aum"
name_in_list = [each_letter for each_letter in name]
print(name_in_list)


double_in_range = [num * 2 for num in range(1, 5)]
print(double_in_range)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)


all_caps_names = [name.upper() for name in names if len(name) > 5]
print(all_caps_names)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)


list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)


with open("./file1.txt") as file_1:
    file_1_nums = file_1.readlines()
    print(f"file 1 numbers: {file_1_nums}")

with open("./file2.txt") as file_2:
    file_2_nums = file_2.readlines()
    print(f"file 2 numbers: {file_2_nums}")

result = [int(num) for num in file_1_nums if num in file_2_nums]
print(result)