import random

names_list = ["Alex", "Beth", "Carol", "Ada", "Alisson"]
# Adding a random grade to each person on that list using dict-comprehension.
students_grades = {name: random.randint(0, 100) for name in names_list}
print(students_grades)

passed_students = {student: grade for (student, grade) in students_grades.items() if grade >= 60}
print(passed_students)
#---------------------------------------------------------------------------------------------------------
#Challenge 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
splitted_setence = sentence.split()
print(splitted_setence)
result = {word: len(word) for word in splitted_setence}
print(result)

#---------------------------------------------------------------------------------------------------------
#Challenge 2
#Celcius to Fhr formula: (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = { weekday: (temperature_in_c * 9/5) + 32 for(weekday, temperature_in_c) in weather_c.items()}

print(weather_f)


