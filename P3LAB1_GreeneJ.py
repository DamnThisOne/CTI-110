
money = float(input("Enter amount of money as a float: $"))

Mon_Int = int(money * 100)


bill = Mon_Int // 100
remain_Mon = Mon_Int % 100
print("Dollars", bill)

quarts = remain_Mon // 25
remain_Mon = remain_Mon % 25
print("Quarters", quarts)

dimes = remain_Mon // 10
remain_Mon = remain_Mon % 10
print("Dimes", dimes)

nickles = remain_Mon // 5
remain_Mon = remain_Mon % 5
print("Nickles", nickles)

penny = remain_Mon // 1
remain_Mon = remain_Mon % 1
print("Pennies", penny)

