#BMI calculator
height = float(input("enter your height"))
weight = float(input("enter your weight"))

bmi = round(weight / (height**2))
print("your BMI is"(bmi))

if bmi < 18.5:
    print(f"You are underweight{bmi}")
elif 18.5 <= bmi <25:
    print(f"you have a normal weight wiht a BMI of {bmi}")
elif 25 <= bmi < 30:
    print(f"you are obese with a BMI of {bmi}")
else:
    print(f"you are extremely & clinically obese with a BMI of {bmi}")
