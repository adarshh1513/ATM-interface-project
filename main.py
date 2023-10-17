import random
import sys
from ascii import ascii_art

class ATM():
    #transaction_list=[]
    #constructor of ATM class that gives a name, account number, and sets the balance to 0 initially
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    #account detail class prints username in Upper case and prints account number along with balance     
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Rupees. {self.balance}\n")
    #function to deposit the money, in which balance is incremented everytime and returning amount and balance everytime
    #so that transaction history can be maintained
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: ", self.balance)
        #transaction_list.append(f"Deposited {amount}")
        print()
        #deposited_money=self.amount
        return amount,self.balance #returning tuple of amount and self.balance

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:#checking if amount to be withdrawn is greater than the balance itself
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} Rupees only.")
            print("Amount entered should be lesser than balance.")
            print()
        else:
            self.balance = self.balance - self.amount#if amount is less or equal to the balance, proceed with withdrawal
            print(f"{amount}Rupees withdrawal successful!")
            print("Current account balance:", self.balance)
            #transaction_list.append("")
            print()
            #withdrawn_money = self.amount
            return amount,self.balance#returning a tuple again to maintain the transaction history
    #def transaction_history(self):
        #print(transaction_list)
 
    def check_balance(self):
        print("**********************************")
        print(" Available balance: ", self.balance)
        print("**********************************")
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Transaction History
            6. Exit
        *********************
        """)
        #deposit_list=[]
        #withdraw_list=[]
        transaction_list=[]#creating a empty list to maintain all the transaction history of withdrawal and deposit and appending them to this empty list
        while True:
            
            try:
                option = int(input("Select Any One: \nOption 1\nOption 2\nOption 3\nOption 4\nOption 5\nOption 6\nEnter Your Option Here: "))
            except:
                print("Error: Enter 1, 2, 3, 4, 5 or 6 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Rupees): "))
                    deposition,balance = atm.deposit(amount)
                    transaction_list.append(f"Deposited: Rupees {deposition}, Balance: Rupees {balance}")
                    #print(transaction_list)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Rupees): "))
                    withdrawal,balance = atm.withdraw(amount)
                    transaction_list.append(f"Withdrew: Rupees {withdrawal},Balance: Rupees {balance}")
                    #print(transaction_list)
                elif option == 5:
                    print("Transaction History from latest transaction to the oldest")
                    print(transaction_list[::-1])
                    #print(deposit_list)
                    
                    
                elif option == 6:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Rupees.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    sys.exit()
        
                 
 
print("*********WELCOME TO THE ATM*********")
print("____________________________________\n")
print(ascii_art)
print("---------CREATE YOUR ACCOUNT--------")
name = input("Your name: ")
account_number = input("Your account number: ")
print("Account successfully created ......\n")
 
atm = ATM(name, account_number)
 
while True:
    trans = input("Do you want to do any transaction?(Yes/No): ").lower()
    if trans == "yes":
        atm.transaction()
    elif trans == "no":
        print("""
    -------------------------------------
   |       Thanks for choosing us        |
   |          Visit us again!            |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")