# Banking Project 
import csv
            
# Casher class
class Cashier:
    
    @staticmethod    
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
            if first_name.isalpha():
                    break
            else:
                print('First Name MUST contain only of string')
                first_name = input('Enter First name: ')
                
                
        last_name = input('Enter Last name: ')
        while True:
            if last_name.isalpha():
                    break
            else:
                print('Last Name MUST contain only of string')
                last_name = input('Enter your Last name: ')
                
        
        password = input('Enter a Password for the account (9 inputs): ')
        
        while True:
            if password != '' and len(password) == 9 :

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
                writer.writerow([account_id, first_name, last_name, password, initial_checking_balance, initial_saving_balance, 'activated', 0])
        print('Customer account added successfully!')

               
# Accounts class               
class Accounts:
    def __init__(self, account_id, password, account_type, checking_amount, saving_amount, transfer_from, transfer_to, target_id , overdraft_limit, overdraft_fee) :
        self.account_id = account_id
        self.password = password
        self.account_type = account_type
        self.checking_amount = checking_amount
        self.saving_amount = saving_amount
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to
        self.target_id = target_id 
        self.overdraft_limit = overdraft_limit
        self.overdraft_fee = overdraft_fee
        
    def user_login(self):
        
        loggedin = False  
        while loggedin != True:
            self.account_id = input('Account Id: ')
            self.password = input('Account Password: ')
            print('')
            with open('bank.csv','r',newline='')as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == self.account_id and row[3] == self.password:
                        loggedin = True
                        # a welcome contain first name and last name
                        print(f'Welcome back {row[1]} {row[2]}!')
                        break
                else:
                    print('incorrect account id or password!')
                    continue
                         
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
                self.withdraw_money()
                print("")
                                
                                
            elif(selection == "2"):
                self.deposit_money()
                print("")
                                
                            
            elif (selection == "3"):
                self.transfer_money()
                print("")
                                
                                
            elif (selection == "4"):
                print("")
                break
            else:
                print("Invalid choice. Enter a Number choice from '1'-'4'")
                print("")
                                
                    
            
    def withdraw_money(self):
        with open('bank.csv','r',newline='') as file:
            rows = list(csv.reader(file))
            
            for row in rows:
                if row[0] == self.account_id and row[3] == self.password:
                    print('')
                    print(f'Checking account balance: {row[4]}')
                    print(f'Saving account balance: {row[5]}')
                    print('')
                    self.account_type = input('Withdraw from checking/saving): ')
                    if self.account_type.lower() == 'checking':
                        
                        self.checking_amount = input('Enter the amount (int or float): ')
                        try:
                            self.checking_amount = float(self.checking_amount)
                            value = float(row[4])
                            
                            if value - self.checking_amount >= 0:
                                total = value - self.checking_amount
                                new_balance = round( total, 2)
                                
                                for r in rows:
                                    if r[0] == self.account_id:
                                        r[4] = str(new_balance)
                                        print(f'New Checking account balance: {r[4]}')
                        
                            elif value - self.checking_amount >= -100 and self.overdraft_limit < 2:
                                total = value - self.checking_amount 
                                # overdraft fee
                                self.overdraft_fee = self.overdraft_fee + 35
                                total = total - 35
                                self.overdraft_limit = self.overdraft_limit + 1
                                new_balance = round( total, 2)
                                print(f'- Overdraft fee $35!, Overdraft limit {self.overdraft_limit}')
                                for r in rows:
                                    if r[0] == self.account_id:
                                        r[7] = str(self.overdraft_fee)
                                        r[4] = str(new_balance)
                                        print(f'New Checking account balance: {r[4]}')
                                        
                                if new_balance < -100:
                                    print('you cant withdraw more than $100 if your account negative!')
                                    return
                                        
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows) 
                                
                                
                            elif self.overdraft_limit >= 2:
                                for r in rows:
                                    if r[0] == self.account_id:
                                        r[6] = 'not_activated'
                                        r[7] = str(self.overdraft_fee)
                                        
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows) 
                            
                                    
                                print('your account in not activated, u need to pay the fee!')
                                pay_fee = input('you want to pay the fee? (y/n)')
                                if pay_fee == 'y':
                                    for r in rows:
                                        if r[0] == self.account_id:
                                            fee = float(r[7])
                                            
                                            if fee > 0:
                                                print(f'Your overdraft fee is ${fee}')
                                                while True:
                                                    pay_from = input('Do you want to pay fee from (checking/saving): ')
                                                    
                                                    if pay_from.lower() == 'checking':
                                                        value = float(r[4])
                                                        if value >= fee:
                                                            total = value - fee
                                                            r[4] = str(round(total,2))
                                                            print('Fee paid, your account reactivated!')
                                                            r[6] = 'activated'
                                                            r[7] = '0'
                                                            break
                                                        else:
                                                            print('There is no enough money!')
                                                    
                                                    elif pay_from.lower() == 'saving':
                                                        value = float(r[5])
                                                        if value >= fee:
                                                            total = value - fee
                                                            r[5] = str(round(total,2))
                                                            print('Fee paid, your account reactivated!')
                                                            r[6] = 'activated'
                                                            r[7] = '0'
                                                            break
                                                        else:
                                                            print('There is no enough money!')
                                                    else:
                                                        print('you should write (checking/saving) word!')         
                                elif pay_fee =='n':
                                    return
                                    
                                    
                            with open('bank.csv', 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(rows) 
                                
                        except ValueError:
                                    print('The amount MUST contain of number(int of float).')
                                    
                                    

                    if self.account_type.lower() == 'saving':
                        
                        self.saving_amount = input('Enter the amount (int or float): ')
                        try:
                            self.saving_amount = float(self.saving_amount)
                            value = float(row[5])
                            
                            if value - self.saving_amount >= 0:
                                total = value - self.saving_amount
                                new_balance = round( total, 2)
                                
                                for r in rows:
                                    if r[0] == self.account_id:
                                        r[5] = str(new_balance)
                                        print(f'New Saving account balance: {r[5]}')
                        
                            elif value - self.saving_amount >= -100 and self.overdraft_limit < 2:
                                total = value - self.saving_amount 
                                # overdraft fee
                                self.overdraft_fee = self.overdraft_fee + 35
                                total = total - 35
                                self.overdraft_limit = self.overdraft_limit + 1
                                new_balance = round( total, 2)
                                print(f'- Overdraft fee $35!, Overdraft limit {self.overdraft_limit}')
                                for r in rows:
                                    if r[0] == self.account_id:
                                        r[7] = str(self.overdraft_fee)
                                        r[5] = str(new_balance)
                                        print(f'New Saving account balance: {r[5]}')
                                        
                                if new_balance < -100:
                                    print('you cant withdraw more than $100 if your account negative!')
                                    return
                                        
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows) 
                                
                                
                            elif self.overdraft_limit >= 2:
                                for r in rows:
                                    if r[0] == self.account_id:
                                        r[6] = 'not_activated'
                                        r[7] = str(self.overdraft_fee)
                                        
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows) 
                            
                                    
                                print('your account in not activated, u need to pay the fee!')
                                pay_fee = input('you want to pay the fee? (y/n)')
                                if pay_fee == 'y':
                                    for r in rows:
                                        if r[0] == self.account_id:
                                            fee = float(r[7])
                                            
                                            if fee > 0:
                                                print(f'Your overdraft fee is ${fee}')
                                                while True:
                                                    pay_from = input('Do you want to pay fee from (checking/saving): ')
                                                    
                                                    if pay_from.lower() == 'checking':
                                                        value = float(r[4])
                                                        if value >= fee:
                                                            total = value - fee
                                                            r[4] = str(round(total,2))
                                                            print('Fee paid, your account reactivated!')
                                                            r[6] = 'activated'
                                                            r[7] = '0'
                                                            break
                                                        else:
                                                            print('There is no enough money!')
                                                    
                                                    elif pay_from.lower() == 'saving':
                                                        value = float(r[5])
                                                        if value >= fee:
                                                            total = value - fee
                                                            r[5] = str(round(total,2))
                                                            print('Fee paid, your account reactivated!')
                                                            r[6] = 'activated'
                                                            r[7] = '0'
                                                            break
                                                        else:
                                                            print('There is no enough money!')
                                                    else:
                                                        print('you should write (checking/saving) word!')         
                                elif pay_fee =='n':
                                    return
                                    
                                    
                            with open('bank.csv', 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(rows) 
                                
                        except ValueError:
                                    print('The amount MUST contain of number(int of float).')
                            
                             
    def deposit_money(self):
        with open('bank.csv','r',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.account_id and row[3] == self.password:
                    print('')
                    print(f'Checking account balance: {row[4]}')
                    print(f'Saving account balance: {row[5]}')
                    print('')
                    self.account_type = input('Deposit to checking/saving): ')
                    if self.account_type == 'checking' or self.account_type == "Checking":
                        self.checking_amount = input('Enter the amount (int or float): ')
                        try:
                            self.checking_amount = float(self.checking_amount)
                            value = float(row[4])
                            total = value + self.checking_amount
                            new_balance = round( total, 2)
                            with open('bank.csv', 'r', newline='') as file:
                                rows = list(csv.reader(file))
                                for row in rows:
                                    if row[0] == self.account_id:
                                        row[4] = str(new_balance) 
                                        print(f'New Checking account balance: {row[4]}')
                                        break
                        except ValueError:
                                    print('The amount MUST contain of number(int of float).')
                                    
                        with open('bank.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                                    
                    elif self.account_type == 'saving' or self.account_type == "Saving":
                        self.saving_amount = input('Enter the amount (int or float): ')
                        try:
                            self.saving_amount = float(self.saving_amount)
                            value = float(row[5])
                            total = value + self.saving_amount
                            new_balance = round( total, 2)
                            with open('bank.csv', 'r', newline='') as file:
                                rows = list(csv.reader(file))
                                for row in rows:
                                    if row[0] == self.account_id:
                                        row[5] = str(new_balance) 
                                        print(f'New Checking account balance: {row[5]}')
                                        break
                        except ValueError:
                                    print('The amount MUST contain of number(int of float).')
                                    
                        with open('bank.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)

                        
                    else:
                        print('you should write (checking/saving) word!')
                       
    
    def transfer_money(self):
        with open('bank.csv','r',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.account_id and row[3] == self.password:
                    print('')
                    print(f'Checking account balance: {row[4]}')
                    print(f'Saving account balance: {row[5]}')
                    
                    print('')
                    print("SELECT A CHOICE")
                    print("")
                    print("1- Checking Account")
                    print("2- Saving Account")
                    print("3- Exit")
                    print("")
                    
                    self.transfer_from = input("Transfer From: ")
                    
                    if(self.transfer_from  == "1"):
                        print('')
                        print("SELECT A CHOICE")
                        print("")
                        print("1- Saving Account")
                        print("2- Another Account")
                        print("")
                        self.transfer_to = input("Transfer To: ")
                        if self.transfer_to == "1":
                            self.saving_amount = input('Enter the amount (int or float): ')
                            try:
                                self.saving_amount = float(self.saving_amount)
                                value = float(row[5])
                                value2 = float(row[4])
                                total = value + self.saving_amount
                                total2 = value2 - self.saving_amount
                                new_balance_to = round( total, 2)
                                new_balance_from = round( total2, 2)
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    for row in rows:
                                        if row[0] == self.account_id:
                                            row[5] = str(new_balance_to)
                                            row[4] = str(new_balance_from)
                                            print(f'New Saving account balance: {row[5]}')
                                            break
                            except ValueError:
                                print('The amount MUST contain of number(int of float).')
                                
                            with open('bank.csv', 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(rows)
                                
                        # transfer to another account
                        if self.transfer_to == "2":
                            self.checking_amount = input('Enter the amount (int or float): ')
                            try:
                                self.checking_amount = float(self.checking_amount)
                                value = float(row[4])
                                total = value - self.checking_amount
                                new_balance = round( total, 2)
                                    
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    for row in rows:
                                        if row[0] == self.account_id:
                                            row[4] = str(new_balance) 
                                            print(f'New Checking account balance: {row[4]}')
                                                
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)   
                                                             
                                self.target_id = input('Enter the Account Id: ')
                                
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    target_exists = False
                                    for r in rows:
                                        if r[0] == self.target_id:
                                            target_exists = True
                                            break
                                if not target_exists:
                                    print("The account dont exist!")
                                    return 
                                
                                with open('bank.csv','r',newline='') as file:
                                    reader = csv.reader(file)
                                    for row in reader:
                                        if row[0] == self.target_id:
                                            print(f'You are transferring to {row[1]} {row[2]}!')
                                            value = float(row[4])
                                            total = value + self.checking_amount
                                            new_balance = round( total, 2)
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    for row in rows:
                                        if row[0] == self.target_id :
                                            row[4] = str(new_balance) 
                                            print(f'Transfer {self.checking_amount} to {self.target_id } Successfully!')
                                            break
                                        
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)
                            except ValueError:
                                print('The amount MUST contain of number(int of float).')
                                    
                           
                                
                                
                    elif(self.transfer_from  == "2"):
                        print('')
                        print("SELECT A CHOICE")
                        print("")
                        print("1- Checking Account")
                        print("2- Another Account")
                        print("")
                        self.transfer_to = input("Transfer To: ")
                        if self.transfer_to == "1":
                            self.checking_amount = input('Enter the amount (int or float): ')
                            try:
                                self.checking_amount = float(self.checking_amount)
                                value = float(row[4])
                                value2 = float(row[5])
                                total = value + self.checking_amount
                                total2 = value2 - self.checking_amount
                                new_balance_to = round( total, 2)
                                new_balance_from = round( total2, 2)
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    for row in rows:
                                        if row[0] == self.account_id:
                                            row[4] = str(new_balance_to)
                                            row[5] = str(new_balance_from)
                                            print(f'New Checking account balance: {row[4]}')
                                            break
                            except ValueError:
                                print('The amount MUST contain of number(int of float).')
                                
                            with open('bank.csv', 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(rows)
                                
                        if self.transfer_to == "2":
                            self.saving_amount = input('Enter the amount (int or float): ')
                            try:
                                self.saving_amount = float(self.saving_amount)
                                value = float(row[5])
                                total = value - self.saving_amount
                                new_balance = round( total, 2)
                                
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    for row in rows:
                                        if row[0] == self.account_id:
                                            row[5] = str(new_balance) 
                                            print(f'New Saving account balance: {row[5]}')
                                                
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)   
                                                             
                                self.target_id  = input('Enter the Account Id: ')
                                
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    target_exists = False
                                    for r in rows:
                                        if r[0] == self.target_id:
                                            target_exists = True
                                            break
                                if not target_exists:
                                    print("The account dont exist!")
                                    return 
                                
                                with open('bank.csv','r',newline='') as file:
                                    reader = csv.reader(file)
                                    for row in reader:
                                        if row[0] == self.target_id :
                                            print(f'You are transferring to {row[1]} {row[2]}!')
                                            value = float(row[4])
                                            total = value + self.saving_amount
                                            new_balance = round( total, 2)
                                with open('bank.csv', 'r', newline='') as file:
                                    rows = list(csv.reader(file))
                                    for row in rows:
                                        if row[0] == self.target_id :
                                            row[4] = str(new_balance) 
                                            print(f'Transfer {self.saving_amount} to {self.target_id } Successfully!')
                                            break
                                        
                                with open('bank.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)
                                        
                            except ValueError:
                                print('The amount MUST contain of number(int of float).')
                                    
                           
                            
                        
                    elif (self.transfer_from  == "3"):
                        print("Goodbye!")
                        print("")
                        break
                    
                    else:
                        print("Invalid choice. Enter a Number choice from '1'-'3'")
                        print("")
                
                            
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
            Cashier.add_customer_account()
            print("")
            
        elif(selection == "2"):
            acc = Accounts(account_id='', password='', account_type='', checking_amount = 0, saving_amount = 0, transfer_from ='', transfer_to ='', target_id ='' , overdraft_limit = 0, overdraft_fee = 0)
            acc.user_login()
            print("")
            
        elif (selection == "3"):
            print("Goodbye!")
            print("")
            break
        else:
            print("Invalid choice. Enter a Number choice from '1'-'3'")
            print("")
            
        
# for testing
if __name__ == '__main__':  
    Bank.menu()
          
    
    