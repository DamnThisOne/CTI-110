'J.Greene '
'30/09/26'
'P2HW2'
''
ScoreAmnt= int(input("How many scores do you want to enter? "))

scores = []

for num in range(1,ScoreAmnt+1):
    score = float(input(f"Enter score #{num}: "))
    
    while score > 100 or score < 0:
        print("Invalid score entered || Score should be between 0 and 100")
        score = float(input(f"Enter score #{num} in a valid format: "))
    scores.append(score)


avgScore = sum(scores)/len(scores)
Low = min(scores)
High = max(scores)
scores.remove(Low)

Grade = "Grade Error"

if avgScore >= 90:
    Grade = "A"

if avgScore >= 80 and avgScore <= 89:
    Grade = "B"

if avgScore >= 70 and avgScore <= 79:
    Grade = "C"

if avgScore >= 60 and avgScore <= 69:
    Grade = "D"

if avgScore <= 59:
    Grade = "F"
    
print()

print("---------------Results----------------")
print(f'{"Lowest grade":<15}: {Low:.1f}')
print(f'{"Modified list":<15}: {scores}')
print(f'{"Grade average":<15}: {avgScore:.2f}')
print(f'{"Grade":<15}: {Grade}')
print("--------------------------------------")
