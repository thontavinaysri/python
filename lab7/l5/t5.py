#25341a05l1 vinay

balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited successfully")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully")
    else:
        print("Insufficient funds")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 3:
        print("Current Balance =", balance)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

'''output :
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter amount to deposit: 500
Amount deposited successfully

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current Balance = 1500.0

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 2
Enter amount to withdraw: 200
Amount withdrawn successfully

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current Balance = 1300.0

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
Exiting...
'''