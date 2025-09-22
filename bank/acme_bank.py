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
        

if __name__ == '__main__':
    print('---------------------------------> Welcome to the ACME Bank! <---------------------------------')
          
    
    