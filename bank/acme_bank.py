# Banking Project 
import csv
            
# Casher class
class Casher:
    
    
    def __init__(self, account_id, first_name, last_name, password, checking_balance, saving_balance):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_balance = checking_balance
        self.saving_balance = saving_balance
    
        
    def add_customer_account():
        
        print('Fill the following fields: ')
        
        account_id = input('Enter Account Id (5 digits only): ')
        
        while True:
            if account_id.isdigit() and len(account_id) == 5:
            #  with open('bank.csv','a',newline='') as file: 
            #     writer = csv.writer(file)
                # writer.writerow(account_id.split(','))
                break
            else:
                print('Account id MUST contain of 5 unique numbers')
                account_id = input('Enter Account Id (5 digits only): ')
                
            
        first_name = input('Enter First name: ')
        while True:
            # need modify (it write also if the rest in number ex. 383j or j888)
            if not first_name.isdigit():
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
            if not last_name.isdigit():
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
                
        initial_checking_balance = input('Enter initial Checking balance: ')
        while True:
            
            # is_float = isinstance(initial_checking_balance, float)
        
            if initial_checking_balance.isdigit():
            #  with open('bank.csv','a+',newline='') as file: 
            #     writer = csv.writer(file)
                # writer.writerow(initial_checking_balance.split(','))
                break
            else:
                print('Initial checking balance MUST contain of numbers')
                initial_checking_balance = input('Enter initial Checking balance: ')
        
        initial_saving_balance = input('Enter initial Saving balance: ')
        while True:
            
            if initial_saving_balance.isdigit():
            #  with open('bank.csv','a+',newline='') as file: 
            #     writer = csv.writer(file)
                # writer.writerow(initial_saving_balance.split(','))
                break
            else:
                print('Initial checking balance MUST contain of numbers')
                initial_saving_balance = input('Enter initial Checking balance: ')
                
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
                    print(row)
        
        
        
      
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
            2
        elif(selection == "2"):
            print(Accounts.user_login())
            print("")
            break
        elif (selection == "3"):
            print("Goodbye!")
            print("")
            break
        else:
            print("Invalid choice. Enter a Number choice from '1'-'3'")
            print("")
            
        

# if __name__ == '__main__':
    
Bank()
          
    
    