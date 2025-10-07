#This code will apply a discount to a given price based on the user's status.
def apply_discount(price, status):
    if status.lower() == "s":
        discount = 0.05
    elif status.lower() == "f":
        discount = 0.08
    
    else:
        discount = 0.0

    discounted_price = price * (1 - discount)
    return discounted_price
price = float(input("Enter the original price: "))
status = input("Enter your status (s for student, f for faculty): ")
final_price = apply_discount(price, status)
print(f"The final price after  discount is: ${final_price:.2f}")
input("Press Enter to exit")
