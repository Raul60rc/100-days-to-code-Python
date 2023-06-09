# Leap year conditional challenge 

# 2000 / 4 = 500 / Leap year 
#2000 / 100 = 20 / Not a Leap year
#2000 / 400 = 5 / Leap year 

year = int(input("enter the year"))

if year % 4 == 0:
    print(f"The year {year} is a leap")
elif year % 100 == 0:
    print(f"The year {year} is not a leap year")
elif year % 400 == 0:
    print(f"The year {year} is not a leap year")
else: 
    print(f"The year {year} is not a leap year")
   