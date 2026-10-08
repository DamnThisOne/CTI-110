'''
J Greene
24.09.26
Using a dictionary to determine cars mpg.
'''
print(10/4)

garage = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Variables
keys = garage.keys()


print(keys)
print()

CarInpt = input("Enter a vehicle to see it's MPG: ")
print()

mpg= garage[CarInpt]

print("The", CarInpt, "gets", mpg,"mpg.")
print()

miles = float(input(f"How many miles will you drive the {CarInpt}? "))
print()

GalRequire = miles/mpg

print(f"{GalRequire:.2f} gallon(s) of gas is needed to drive the {CarInpt} {miles} miles.")

