import random

grades = ["A's!","B's!","C's.","D's.","F's!?"]
students = ['alice','david','caroline']
for student in students:
    print(student.title())

for student in students:
    print(student.title() + ", that was a great presentation!")
    print("I can't wait to see your next project, " + student.title() + ".\n")



print("Thank you, everyone. You all receive " + random.choice(grades))
