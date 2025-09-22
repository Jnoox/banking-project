# Banking Project 
import csv


            
# Casher class
class Casher:
    
    # initial values 
    first_name = None
    last_name = None
    password = None
    checking_balance = 0.0
    saving_balance = 0.0
    account_id = None
    
    def __init__(self, account_id, first_name, last_name, password, checking_balance, saving_balance):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_balance = checking_balance
        self.saving_balance = saving_balance
    
        
    def add_customer_account():
        print('Fill the following fields: ')
        account_id = int(input('Enter Account Id: '))
        first_name = input('Enter your First name: ')
        last_name = input('Enter your Last name: ')
        password = input('Enter a Password for the account: ')
        checking_balance = float(input('Enter initial Checking balance: '))
        checking_balance = float(input('Enter initial Saving balance: '))
    
# Bank class
class Bank:
    while True:
        print('---------------------------------> Welcome to the ACME Bank! <---------------------------------')
        print("SELECT A CHOICE")
        print("")
        print("1- Add New Customer")
        print("2- Login Into Account")
        print("3- Exit")
        print("-----------------------------------------------><----------------------------------------------")

        selection = input("Enter a choice: ")

        if(selection == "1"):
            print(Casher.add_customer_account())
            print("")
            break
        elif(selection == "2"):
            e2()
            print("")
            break
        elif(selection == "3"):
            e3()
            print("")
            break
        elif (selection == "e7"):
            print("Goodbye")
            print("")
            break
        else:
            print("Invalid choice. Enter a Number choice from '1'-'3'")
            
            
        

# if __name__ == '__main__':
    
Bank()
          
    
    