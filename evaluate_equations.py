#Parentheses in python are used to change the order of operations and follows pemdas just like in math

print( "Equation 1: 4 * 8 + 3" )
        #Equation 1: 4 * 8 + 3
variation1 = (4 * 8) + 3
print( f"Variation 1:(4 * 8) +3: {variation1}"
          )
        #Equation 2: 4 * (8 + 3)
variation2 = 4 * (8 + 3)    
print (f"Variation 2: 4 * (8 + 3): {variation2}")
line = "------------------------------------------------------"
print(line)
#######################################################################

print( "Equation 2: 8 / 200 - 9" )
        
variation1 = (8 / 200) - 9
print( f"Variation 1: (8 / 200) - 9: {variation1}"
          )
       
variation2 = 8 / (200 - 9)    
print (f"Variation 2: 8 / (200 - 9): {variation2:.2f}")
print(line)
#######################################################################

print( "Equation 3: 400 * 8 + 7" )
        
variation1 = (400 * 8) + 7
print( f"Variation 1: (400 * 8) + 7: {variation1}"
          )
       
variation2 = 400 * (8 + 7)    
print (f"Variation 2: 400 * (8 + 7): {variation2}")
print(line)

input("Press Enter to exit.")


    