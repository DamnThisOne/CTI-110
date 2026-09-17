 # J. Greene
 # 17/09/26
 # P1 HW2
 # A program that calculates travel budgets
 
 # Collecting Data (Destination, Money, Gas, Hotel cost, Food cost)
Destination=  input("Enter the destination of your travels:")
Money= input("Enter Budget: ")
GasEst= input("How much money do you have for gas ?")
Hotel= input("How much money do you have for hotels?")
Food= input("How much money do you have for food ?")

#Turns the number inputs into integers so they can be used for calculation
Money= int(Money)
GasEst= int(GasEst)
Hotel= int(Hotel)
Food= int(Food)

# Printing a "reciept" of the expenses
print(" ")
print("*~--| Travel Expenses |--~*")
print("Location:",Destination)
print("Initial budget:",Money)
print("")

total= GasEst + Hotel + Food
budget= Money - total

#Total of gas, hotel, and food costs
print("Fuel:", GasEst)
print("Accomodation:", Hotel)
print("Food:",Food)
print("")
print("Cost total:", total)

print("Remaining Balance", budget)