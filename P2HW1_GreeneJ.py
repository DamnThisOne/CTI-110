 # J. Greene
 # 29/09/26
 # P2HW2
 # A program that calculates travel budgets, reformatted
 
 # Collecting Data (Destination, Money, Gas, Hotel cost, Food cost)
Destination=  input("Enter the destination of your travels: ")
print()
Money= input("Enter Budget: ")
print()
GasEst= input("How much money do you have for gas ? ")
print()
Hotel= input("How much money do you have for hotels? ")
print()
Food= input("How much money do you have for food ? ")
print()

#Turns the number inputs into integers so they can be used for calculation
Money= float(Money)
GasEst= float(GasEst)
Hotel= float(Hotel)
Food= float(Food)

# Printing a "reciept" of the expenses

print(" ")
print("~--| Travel Expenses |--~")
print()
print(f'{"Location:":<20} {Destination}')

print()
print("-------------------------------")
print()
print(f'{"Initial budget:":<20} ${Money:.2f}')
print()

total= GasEst + Hotel + Food
budget= Money - total

#Total of gas, hotel, and food costs

print(f'{"Fuel:":<20} ${GasEst:.2f}')
print(f'{"Accomodation:":<20} ${Hotel:.2f}')
print(f'{"Food:":<20} ${Food:.2f}')
print("")
print("-------------------------------")
print(f'{"Cost total:":<20} ${total:.2f}')
print(f'{"Remaining Funds:":<20} ${budget:.2f}')