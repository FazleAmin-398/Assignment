# Result cards: marks decide the grade (A, B, C, Fail).
input_marks = float(input("Enter your marks: "))
if input_marks >= 90:
    print("Grade: A")
elif input_marks >= 80:
    print("Grade: B")
elif input_marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")
