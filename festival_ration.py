number_colonists = ""
while type(number_colonists) is not int:
    try:
        var1 = input("How many colonists?")
        var1 = int(number_colonists)
    except ValueError:
        print("Invalid input, please enter integers only.")

total_food_rations = ""
while type(total_food_rations) is not int:
    try:
        var2 = input("Enter total food rations available:")
        var2 = int(var2)
    except ValueError:
        print("Invalid input, please enter integers only.")
message = f"Origanal supply: {total_food_rations}"
print (message)
message = f"Ration allocation: {number_colonists * 4} (4 per colonist)"
print (message)
if total_food_rations >= number_colonists * 4:
    total_food_rations = total_food_rations - (number_colonists * 4)
    message = f"Festival Stockpile remaing: {total_food_rations}"
    print (message)