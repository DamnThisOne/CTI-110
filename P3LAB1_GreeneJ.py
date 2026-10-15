
money = float(input("Enter amount of money as a float: $"))

Mon_Int = int(money * 100)


bill = Mon_Int // 100
remain_Mon = Mon_Int % 100
print("Dollars", bill)

quarters = remain_Mon // 25
remain_Mon = remain_Mon % 25
print("Quarters", quarters)

dimes = remain_Mon // 10
remain_Mon = remain_Mon % 10
print("Dimes", dimes)

nickles = remain_Mon // 5
remain_Mon = remain_Mon % 5
print("Nickles", nickles)

pennies = remain_Mon // 1
remain_Mon = remain_Mon % 1
print("Pennies", pennies)

print()

def MoneySpread(coin, cointype):
    if coin > 0:
        if coin == 1:
            print(f"1 {cointype}")
        if coin > 1:
            print(f"{coin} {cointype}s")
            
MoneySpread(bill, "dollar")
MoneySpread(quarters,"quarter")
MoneySpread(dimes,"dime")
MoneySpread(nickles, "nickle")
MoneySpread(pennies, "penny")

