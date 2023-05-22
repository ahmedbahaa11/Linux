######################################
# Project : ATM Machine              #
# Auther : Ahmed Bahaa Nasr          # 
# Date : 6/5/2023                    # 
######################################
# Account holders
account_holders = [
    ("Ahmed Bahaa", 1214 , 5000),
    ("Wafaa Muhamed", 1234 , 10000),
    ("Islam Ashraf", 1111 , 7500),
    ("Israa Ahmed", 2222 , 32000),
    ("Alaa Elnaggar", 3333 , 50000),
]

import os
# Function to get account holder's index
def get_index(id):
    for i in range(len(account_holders)):
        if account_holders[i][1] == id :
            return i
    return None

# ATM operations 
while True:
    print("***************************************")
    print("***************************************")
    print("**     Welcome to My ATM Machine     **")
    print("**     Auther : Ahmed Bahaa Nasr     **")
    print("**      Embedded Linux Software      **")
    print("***************************************")
    print("***************************************")
    print("=======================================")
    print("Welcome to the ATM")
    print("Enter (0) to Exit..")
    print("=======================================")
    id = int(input("Please enter your account number: "))
    if id == 0 :
        os.system('cls' if os.name == 'nt' else 'clear')
        print( "==========================" )
        print( "==========================" )
        print( "=====    Good Bey    =====" )
        print( "==========================" )
        print( "==========================" )
        break
    index = get_index(id)
    if index is not None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===========================")
        print("Hello, ", account_holders[index][0])
        while True:
            print("===========================")
            print("What would you like to do?")
            print("(1) View balance")
            print("(2) Withdraw money")
            print("(3) Deposit money")
            print("(0) Exit")
            print("===========================")
            choice = int(input("Enter your choice: "))
            print("===========================")
            if choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===========================")
                print("Your balance is ",account_holders[index][2])
            elif choice == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=================================")
                amount = int(input("Enter amount to withdraw: "))
                if amount <= account_holders[index][2]:
                    account_holders[index] = (account_holders[index][0], account_holders[index][1], account_holders[index][2] - amount)
                    print("Withdrawal successful. Your new balance is ",account_holders[index][2])
                    print("=======================================================")
                else:
                    print("===========================")
                    print("Insufficient funds")
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=================================")
                amount = int(input("Enter amount to deposit: "))
                account_holders[index] = (account_holders[index][0], account_holders[index][1], account_holders[index][2] + amount)
                print("Deposit successful. Your new balance is ",account_holders[index][2])
                print("=======================================================")
            elif choice == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===================================")
                print("Invalid choice. Please try again.")
    else:
        print("=========================================")
        print("Invalid account number. Please try again.")