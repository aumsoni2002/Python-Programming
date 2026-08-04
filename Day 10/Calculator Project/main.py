from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dic = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

print(logo)
is_continue = "n"
f_num = 0.0
s_num = 0.0
result = 0.0
while True:
    if is_continue == "n":
        f_num = float(input("What's the first number?: "))
    else:
        f_num = result
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    s_num = float(input("What's the second number?: "))
    calculation = operations_dic[operation]
    result = calculation(f_num, s_num)
    print(f"{f_num} {operation} {s_num} = {result}")
    is_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")