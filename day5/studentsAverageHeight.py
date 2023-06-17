# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above👆


#fix this code// the code below is giving total sum but it's not divding neither giving a round number

for student in student_heights:
    student = int(input("number of students"))
    total_height = sum(student_heights)
    average_height = total_height / student
    round(average_height)
    print(average_height)

#Write your code below this row 👇