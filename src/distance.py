import math
import time
"""Unit Converter"""
#Welcome and variable setting
print ("Welcome to Sam's Unit Converter")
cat = str(input("Which category would you like to convert? we support length(l) and Weight(w):  "))
if cat == ("l"):
	unit1 = str(input("Which unit would you like to convert from: "))
	unit2 = str(input("Which unit would you like to convert to: "))
	num1 = int(input("Enter your value: " ))

    ##Calculations

if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    print(ans)
