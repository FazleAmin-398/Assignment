# Challenge — Class result sheet
# Store marks as {"Ali": [80, 72, 91], "Sara": [95, 88, 90], ...} for at least 5
# students. Print each student’s total and average, the class topper, and a set of all students
# who scored below 40 in any subject
std_marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [35, 42, 50],
    "Zara": [60, 75, 80],
    "Bilal": [45, 38, 55]
}
for student, marks in std_marks.items():
    total = sum(marks)
    average = total / len(marks)
    print(student, "\nTotal Marks=", total, ", Average =", average)
    
       