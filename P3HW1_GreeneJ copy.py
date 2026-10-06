'J.Greene '
'30/09/26'
'P2HW2'
''
print()
Mod1= input("Enter grade for Module 1: ")
Mod2= input("Enter grade for Module 2: ")
Mod3= input("Enter grade for Module 3: ")
Mod4= input("Enter grade for Module 4: ")
Mod5= input("Enter grade for Module 5: ")
Mod6= input("Enter grade for Module 6: ")

Mod1= float(Mod1)
Mod2= float(Mod2)
Mod3= float(Mod3)
Mod4= float(Mod4)
Mod5= float(Mod5)
Mod6= float(Mod6)

gradeList =[Mod1,Mod2,Mod3,Mod4,Mod5,Mod6]
avgScore = sum(gradeList)/len(gradeList)
Low = min(gradeList)
High = max(gradeList)
print()

print("---------------Results----------------")
print(f'{"Lowest grade:":<20} {Low:.1f}')
print(f'{"Highest grade:":<20} {High:.1f}')
print(f'{"Sum of grades":<20} {sum(gradeList):.1f}')
print(f'{"Grade average:":<20} {avgScore:.2f}')
print("--------------------------------------")

if avgScore >= 90:
    print("Grade: A")

if avgScore >= 80 and avgScore <= 89:
    print("Grade: B")

if avgScore >= 70 and avgScore <= 79:
    print("Grade: C")

if avgScore >= 60 and avgScore <= 69:
    print("Grade: D")

if avgScore <= 59:
    print("Grade: F")