weight = input("enter your weight: ")
unit = input("kilo or pounds? (K/L): ")

if unit == "K" or unit == "k":
    
    converted = float(weight) / 0.45
    
    print("weight in lbs: ", converted)
elif unit == "L" or unit == "l":
    
    converted = float(weight) * 0.45
    print("weight in k: ", converted)
else:
    print("invalid")

    
