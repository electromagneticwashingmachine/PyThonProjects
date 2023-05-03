student_scores = {
    "Harry": 81, # Exceeds Expectations
    "Ron": 78, # Acceptable
    "Hermione": 99, # Outstanding
    "Draco": 74, # Acceptable
    "Neville": 62, # Fail
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"



print(student_grades)
