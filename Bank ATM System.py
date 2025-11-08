#❌❌1.Bank ATM System❌❌


Bank_ATM_System = {
    11115: {"Password":1111, "Balance":5000},
    11116: {"Password":1111, "Balance":50000},
    11117: {"Password":1111, "Balance":10000},
    11118: {"Password":1111, "Balance":13320},
    11114: {"Password":1111, "Balance":123555},
    11113: {"Password":1111, "Balance":675543},
    11112: {"Password":1111, "Balance":123334},
    11111: {"Password":1111, "Balance":98998}
}

while True:         #USER_ID
    try:
        User_ID = int(input("Enter your 5-digit User ID: "))
        if 10000 <= User_ID <= 99999:
            if User_ID in Bank_ATM_System:            ##Check if user exists in database
             break
            else:
                print("❌ Incorrect User ID. Please try again.")    
        else:
            print("❌ User ID must be exactly 5 digits.")
    except ValueError:
        print("⚠️ User ID should contain numbers only!")


import getpass
while True:        #PASSWORD
    try:
        Password = getpass.getpass("Enter your 4-digit password: ")
        if Password.isdigit() and 1000<= int(Password) <=9999:
            Password = int(Password)
            if Password ==Bank_ATM_System[User_ID]["Password"]:
              break
            else:
                print("❌ Incorrect password. Please try again!")
        else:
            print("❌ Password must be exactly 5 digits.")
    except ValueError:
        print("⚠️  User ID should contain numbers only!")

print("\n✅Login Successeful!")

while True:
    print("\n ========= ATM MENU =========")
    print("1. Check balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Select the service: ")

    if choice == "1":
        print(f"💰 Your currnt balance: ₹{Bank_ATM_System[User_ID]['Balance']}")

    elif choice == "2":
        Amount = float(input("Enter amount to deposit: ₹"))
        Bank_ATM_System[User_ID]["Balance"] += Amount              # Update the balance
        Current_Amount = Bank_ATM_System[User_ID]["Balance"]           # Store current balance
        print(f"{Amount} deposited successfully.")
        print(f"Your current balance is ₹{Current_Amount} ")

    elif choice == "3":
        Amount= float(input("Enter amount to withdraw: ₹"))
        if Amount <= Bank_ATM_System[User_ID]["Balance"]:
            Bank_ATM_System[User_ID]["Balance"] -= Amount
            Current_Balance = Bank_ATM_System[User_ID]["Balance"]
            print(f"💰₹{Amount} withdrawn successfully.")
            print(f"Your current balance is: ₹{Current_Balance}")

        else:
            print("❌Insufficient Balance.")

    elif choice == "4":
        print("👋 Thank you for using our ATM!")
        break

    else:
         print("⚠️ Invalid choice. Try again.")    








