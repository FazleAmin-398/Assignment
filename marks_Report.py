# Write average(marks) , grade(avg) (reuse your Part 2 table) and report(name, marks)
# that uses the other two and returns a one-line result string. Use them on 3 students
#function to calculate average of marks
def average(marks):
    return sum(marks) / len(marks)
#function to calculate grade based on average marks
def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
    
#function to report name, average marks and grade
def report(name, marks):
    avg = average(marks)
    gr = grade(avg)
    print("Name:", name,",","Average:", round(avg, 2), ",","Grade:", gr)
    #calling report function for 3 students
report("Ali", [80, 72, 91])
report("Sara", [95, 88, 90])
report("Ahmed", [35, 42, 50])