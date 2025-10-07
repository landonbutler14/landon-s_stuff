#getting variables
while True:
    try:
        starting_population = int(input("Enter the starting number of bacteria: "))
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        
while True:
    try:
        hourly_growth_rate = float(input("Enter the hourly growth rate as a decimal: "))
        break
    except ValueError:
        print("Invalid input. Please enter a decimal number.")
while True:
    try:
        hours = int(input("Enter the number of hours to simulate: "))
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

population_history = []
current_population = starting_population
#Divides hours into a list of hours
list_of_hours = list(range(0, hours + 1))
#Calculates population for each hour and adds to list
for hour in list_of_hours:
    current_population = float(starting_population * hourly_growth_rate ** hour)
    population_history.append(current_population)

for hour, pop in zip(list_of_hours, population_history):
    print(f"Hour {hour}: {pop:.2f}")

    







