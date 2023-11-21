print("Welcome to the Tip Calculator\n")
total_bill = float(input("What was the total bill? $")) 
tip_percentage = float(input("What percentage tip would you like to give? "))
split_bill_people = float(input("How many people to split the bill? "))

tip_decimal = ((tip_percentage) / 100)

dollar_tip = (total_bill * tip_decimal)

each_person_pays = ((total_bill + dollar_tip) / split_bill_people)

print(f"Each person should pay ${round(each_person_pays,2)}")