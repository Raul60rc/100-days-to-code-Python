print ("welcome to the tip calculator")

bill = float(input("what is your total bill in $?"))
tip = int("what % tip you want to pay?")
people = int(input("how many people are you?"))

tip_in_percantage = tip / 100

bill_with_tip = bill + tip / people
print(bill_with_tip)

