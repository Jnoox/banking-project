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
    
    def __init__(self, first_name, last_name, password, checking_balance, saving_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_balance = checking_balance
        self.saving_balance = saving_balance
    
        
    def add_customer_account(self):
        pass
    
# Bank class
class Bank:
    while True:
        print('---------------------------------> Welcome to the ACME Bank! <---------------------------------')
        print("SELECT A CHOICE")
        print("")
        print("1- Add New Customer")
        print("2- Log in ")
        print("3- Exit")
        print("")

        selection = input("Enter a choice: ")

        if(selection == "1"):
            e1()
            break
        elif(selection == "2"):
            e2()
            break
        elif(selection == "3"):
            e3()
            break
        elif(selection == "e7"):
            print("Goodbye")
            break
        else:
            print("Invalid choice. Enter a Number choice from '1'-'3'")
            
        

# if __name__ == '__main__':
    
Bank()
          
    
    