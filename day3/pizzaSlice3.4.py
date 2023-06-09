size = input("what size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
price = 0
# small pizza : $15
# medium pizza : $20
# large pizza : $25
# Peperoni for small pizza: +$2
# pepperoni for medium or large pizza $3+
# Extra Cheese for any pizza $1+

print("What pizza would you like?")
if size == "S":
    price = 15
    print(f"the price is ${price}")
elif size == "M":
    price = 20
    print(f"the price is ${price}")
elif size == "L":
    price = 25
    print(f"the price is ${price}")
    if add_pepperoni == "Y":
        price = 2
    print(f"it's going to be ${price}extra")
