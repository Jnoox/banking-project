# Banking Project 
import csv
            
# Casher class
class Casher:
    
    # def __init__(self, account_id, first_name, last_name, password, checking_balance, saving_balance):
    #     self.account_id = account_id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.password = password
    #     self.checking_balance = checking_balance
    #     self.saving_balance = saving_balance
    
        
    def add_customer_account():
        
        print('Fill the following fields: ')
        
        account_id = input('Enter Account Id (5 digits only): ')
        while True:
            if account_id.isdigit() and len(account_id) == 5:
                with open('bank.csv','r',newline='')as file:
                    reader = csv.reader(file)
                    ids = [row[0] for row in reader if row]
                if account_id in ids:
                            print('Account ID already exists, please use another one.')
                            account_id = input('Enter Account Id (5 digits only): ')
                else:
                    break
            else:
                print('Account id MUST contain of 5 unique numbers')
                account_id = input('Enter Account Id (5 digits only): ')
                
            
        first_name = input('Enter First name: ')
        while True:
            # need modify (it write also if the rest in number ex. 383j or j888)
            if first_name.isalpha():
                # with open('bank.csv','a',newline='') as file: 
                #     writer = csv.writer(file )
                    # writer.writerow(first_name.split(','))
                    break
            else:
                print('First Name MUST contain only of string')
                first_name = input('Enter First name: ')
                
                
        last_name = input('Enter Last name: ')
        while True:
            # need modify (it write also if the rest in number ex. 383j or j888)
            if last_name.isalpha():
                # with open('bank.csv','a',newline='') as file: 
                #     writer = csv.writer(file )
                    # writer.writerow(last_name.split(','))
                    break
            else:
                print('Last Name MUST contain only of string')
                last_name = input('Enter your Last name: ')
                
        
        password = input('Enter a Password for the account (9 inputs): ')
        
        while True:
            if password != '' and len(password) == 9 :
                
                # with open('bank.csv','a+',newline='') as file: 
                #     writer = csv.writer(file)
                    # writer.writerow(password.split(','))
                    break
            else:
                print('Password MUST contain of at least 9 inputs')
                password = input('Enter a Password for the account (9 inputs): ')
                
        initial_checking_balance = input('Enter initial Checking balance (int or float): ')
        while True:
            try:
                initial_checking_balance = float(initial_checking_balance)
                break
            except ValueError:
                print('Initial checking balance MUST contain of number(int of float).')
                initial_checking_balance = input('Enter initial Checking balance (int or float): ')
        
        initial_saving_balance = input('Enter initial Saving balance (int or float): ')
        while True:
            try:
                initial_saving_balance = float(initial_saving_balance)
                break
            except TypeError:
                print('Initial checking balance MUST contain of number (int or float).')
                initial_saving_balance = input('Enter initial Checking balance (int or float): ')
                
        with open('bank.csv','a',newline='') as file: 
                writer = csv.writer(file)        
                writer.writerow([account_id, first_name, last_name, password, initial_checking_balance, initial_saving_balance])
        print('Customer account added successfully!')

               
# Accounts class               
class Accounts:
    def __init__(self, account_id , password):
        self.account_id = account_id
        self.password = password
        
    def user_login():
        
        loggedin = False
        
        while loggedin != True:
            account_id = input('Account Id (Must contain of 5 digits): ')
            password = input('Account Password (Must contain of 9 inputs): ')
            with open('bank.csv','r',newline='')as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == account_id and row[3] == password:
                        loggedin = True
                        # a welcome contain first name and last name
                        print(f'Welcome back {row[1]} {row[2]}!')
                        while True:
                            print("SELECT A CHOICE")
                            print("")
                            print("1- Withdraw Money")
                            print("2- Deposit Money")
                            print("3- Transfer Money")
                            print("4- Logout")
                            print("")
                            
                            selection = input("Enter a choice: ")
                            if(selection == "1"):
                                print(Accounts.withdraw_money())
                                print("")
                                
                            elif(selection == "2"):
                                print(Accounts.deposit_money())
                                print("")
                            
                            elif (selection == "3"):
                                print(Accounts.transfer_money())
                                print("")
                                
                            elif (selection == "4"):
                                 print("")
                                 break
                                # print(Bank.menu())
                                # break
                            else:
                                print("Invalid choice. Enter a Number choice from '1'-'4'")
                                print("")
                                
                                
                else:
                    print('incorrect account id or password!')
                     
            # to access to place in the row i can use row[index value]
             # assess this row!print(row)
            
    def withdraw_money():
        print('hi w')
        
    
    def deposit_money():
        print('hi d')
        
    
    def transfer_money():
        print('hi t')
        
            
      
# Bank class
class Bank:
    
 def menu():
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
            
        elif(selection == "2"):
            print(Accounts.user_login())
            print("")
            
        elif (selection == "3"):
            print("Goodbye!")
            print("")
            break
        else:
            print("Invalid choice. Enter a Number choice from '1'-'3'")
            print("")
            
        
# for testing
# if __name__ == '__main__':
    
Bank.menu()
          
    
    