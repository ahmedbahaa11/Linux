# ATM Machine
# Ahmed Bahaa Nasr

# Account holders
account_holders = [
    ("Ahmed Bahaa", 1214 , 5000),
    ("Wafaa Muhamed", 1234 , 10000),
    ("Islam Ashraf", 1111 , 7500),
    ("Israa Ahmed", 2222 , 32000),
    ("Alaa Elnaggar", 3333 , 50000),
]

# Function to get account holder's index
def get_index(id):
    for i in range(len(account_holders)):
        if account_holders[i][1] == id:
            return i
    return None

# ATM operations 
while True:
    print("Welcome to the ATM")
    id = int(input("Please enter your account number: "))
    index = get_index(id)
    if index is not None:
        print("Hello, ", account_holders[index][0])
        while True:
            print("What would you like to do?")
            print("1. View balance")
            print("2. Withdraw money")
            print("3. Deposit money")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Your balance is ",account_holders[index][2])
            elif choice == 2:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= account_holders[index][2]:
                    account_holders[index] = (account_holders[index][0], account_holders[index][1], account_holders[index][2] - amount)
                    print("Withdrawal successful. Your new balance is ",account_holders[index][2])
                else:
                    print("Insufficient funds")
            elif choice == 3:
                amount = int(input("Enter amount to deposit: "))
                account_holders[index] = (account_holders[index][0], account_holders[index][1], account_holders[index][2] + amount)
                print("Deposit successful. Your new balance is ",account_holders[index][2])
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid account number. Please try again.")