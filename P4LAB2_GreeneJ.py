# J. Greene
#10/27/26
#Loops display multiplication
runAgain = "yes"
while runAgain == "yes":
    InputNum = int(input("Enter any integer: "))
    
    if InputNum >= 0:
        for i in range(1,12+1):
            print(f'{InputNum} * {i} = {InputNum * i}')
    
    runAgain = input("Run the program again? ")
    
print("Program has ended")