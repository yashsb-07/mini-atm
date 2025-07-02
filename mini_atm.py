correct_pin = 1234
balance = 1000
attempt = 5

while attempt > 0:
    pin = int(input("Enter your 4-digit pin: "))
    if pin == correct_pin:
        print("Access Granted.. !")
        while True:
            print("##### Mini ATM menu #####")
            print("1. Show balance")
            print("2. Diposit")
            print("3. Withdraw")
            print("4. Exit")
            
            ch = int(input("Enter your chioce: "))

            if ch == 1:
                print("Your current balance is RS. ", balance)
                
            elif ch == 2:
                amt = int(input("Enter your depoit amount: "))
                if amt > 0:
                    balance += amt
                    print("Rs.", amt, "is succesfully diposited.")
                else:
                    print("Inavlid amount: Please enter valid amount.")

            elif ch == 3:
                amt = int(input("Enter you withdraw amount: "))
                if amt > 0 and amt <= balance:
                    balance -= amt
                    print("Rs. ", amt, "Withdraw succesfully")
                elif amt > balance:
                    print("Insufficient balance.")
                    
                else:
                    print("Invalid amount.")
                    
            elif ch == 4:
                print("Thank you for visiting MINI ATM.. !")
                break
            
            else:
                print("Incorrect ooption: Please choose correct option.")
        break
    else:
        attempt -= 1
        print(f"Error: please enter valid pin. attempts {attempt}")
        if attempt == 0:
            print("Too many incorrect attempts.. try again letter.")
        


        

        