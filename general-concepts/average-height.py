# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
heights_counter = 0
heights_sum = 0

for i in student_heights:
    heights_sum += i
    heights_counter+=1

heights_average = round(heights_sum / heights_counter)

print(f"The sum of all the values was: {heights_sum}")
print(f"The number of values assessed was: {heights_counter}")
print(f"The average height is: {heights_average}")