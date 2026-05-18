class Bank_Transactions:
    def __init__(self):
        self.account_number = int(input("enter account number: "))
        self.balance = int(input("enter balance: "))

    def deposit_amt(self):
        amount = int(input("enter amount to deposit: "))
        self.balance += amount
        print("Deposited Successfully")
        print(f"The deposited amount was {amount}")

    def withdraw_amt(self):
        amount = int(input("enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
            print(f"The withdrawal amount was {amount}")
        else:
            print("Entered amount exceeded the balance amount")
        
    def display_details(self):
        print("The Bank account details are: ")
        print("Account Number: ",self.account_number)
        print("Total Balance: ",self.balance)
        

#creating object
bank = Bank_Transactions()
while True:
    print("Bank Transaction Information: \n")
    print("1. Display Bank Details")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")
    option = int(input("enter option between 1 to 4: "))
    if option == 1:
        bank.display_details()
        
    elif option == 2:
        bank.deposit_amt()
        
    elif option == 3:
        bank.withdraw_amt()
        
    elif option == 4:
        print("Exiting...")
        break
    else:
        print("Invalid option")
