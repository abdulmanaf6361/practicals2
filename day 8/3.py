# Take marks (0-100) as input. Print the grade: A (90-100), B (75-89), C (60-74), D (40-59), Fail (below 40).

marks = int(input("Enter your marks\n"))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >= 60 and marks <= 74:
    print("Grade C")
elif marks >= 40 and marks <= 59:
    print("Grade D")
else:
    print("Fail")