student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    grade = student_scores[key]

    if grade <= 70:
        student_grades[key] = "Fail"
    
    elif grade < 81:
                student_grades[key] = "Acceptable"
        
    elif grade < 91:
                student_grades[key] = "Exceeds Ecpectations"
        
    elif grade > 90:
                student_grades[key] = "Outstanding"
        

# 🚨 Don't change the code below 👇
print(student_grades)

#This is the scoring criteria:

#> Scores 91 - 100: Grade = "Outstanding"

#> Scores 81 - 90: Grade = "Exceeds Expectations"

#> Scores 71 - 80: Grade = "Acceptable"

#> Scores 70 or lower: Grade = "Fail"
