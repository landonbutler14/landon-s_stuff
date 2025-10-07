
def split_even_odd(numbers):   
    #Two variables as lists to hold even and odd numbers
    even_numbers = []
    odd_numbers = []
    #Loop through the list and check if each number is even or odd
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number) #If even adds to even list
        else:
            odd_numbers.append(number) #Same
    
    return even_numbers, odd_numbers

numbers = input("Enter a list of numbers separated by spaces: ").split() #Gets iput and puts into list
numbers = [int(num) for num in numbers] #Converts each item in list to integer so math works
even, odd = split_even_odd(numbers)
print("Original list:", numbers)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")    
input("Press Enter to quit ")

