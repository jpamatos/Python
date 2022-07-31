# A simple tip calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
pay = (bill + (bill * tip) / 100) / people
pay = round(pay, 2)
print(f"Each person should pay: ${pay}")