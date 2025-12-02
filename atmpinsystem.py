balance = 8000
pin = 7869

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("Your balance is:", balance)
    
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print("Congratulations! Amount withdrawn.")
        print("New balance is:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Incorrect PIN! Access denied.")