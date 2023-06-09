child_height = int(input("enter the child's height in CM"))
bill = 0 

if child_height >= 120:
    
    print ("You are eligible to ride")
    age = int(input("enter your age"))
    if age < 12:
        bill = 5
        print(f"you have to pay ${bill}")
    elif age >= 12 and age < 18:
        bill = 7
        print(f"you have to pay ${bill}")
    else:
        bill = 12
        print(f"You have to pay ${bill}") 
    photo = input("do you want a photo Y or N.")
    if photo == "Y":
        bill =+ 3
        
    print(f"your final bill is ${bill}")   
     
else:
 print ("you are not eligible to ride")