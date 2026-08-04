print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill?"))
tip_in_percent = float(input("How much tip would you like to give? 10, 12 or 15?"))
total_people = int(input("How many people to split the bill?"))

each_person_bill = total_bill / total_people
each_person_tip = each_person_bill * tip_in_percent / 100
each_person_pay = round(each_person_bill + each_person_tip, 2)

print(each_person_pay)