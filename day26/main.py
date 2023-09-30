name = "Rahul"

letter_list = [letter for letter in name]
print(letter_list)

range_list =  [num * 2 for num in range(1,5)]
print(range_list)


names = ["Alex","Beth","Caroline","David","Ethan","Frank","John"]

short_names = [item.upper() for item in names if len(item) >= 5]
print(short_names)


