total_bill = None
percentage = None
party = None
amount_to_pay = None

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
party = input("How many people to split the bill? ")

amount_to_pay = (float(total_bill) + float(total_bill)*int(percentage)/100) / int(party)
print(f"Each person should pay: ${round(amount_to_pay,2)}")