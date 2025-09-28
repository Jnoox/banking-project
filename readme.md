
ACME Bank System

Overview:

ACME Bank is a simple banking system implemented in Python. It allows a Cashier to add new customers, and enables customers to log in to their accounts to manage their finances. All account information is stored in a CSV file (bank.csv), supporting banking operations (withdraw money, deposit money, transfer money).


---------------------------------------------------------------------------------------------><---------------------------------------------------------------------------------------------------------------

Features:
Cashier:
Add new customer accounts.

Customer:
Login with account ID and password.
Perform banking operations:
Withdraw Money (with overdraft handling) - Deposit Money - Transfer Money (between checking and saving accounts, or to another account)

---------------------------------------------------------------------------------------------><---------------------------------------------------------------------------------------------------------------

Code Highlights
The parts of the code I’m proud of:

add_customer_account() – validates inputs (ID, name, password, balances) and safely writes to CSV.

user_login() – handles login and displays a personalized welcome message. After checking login, the customer can use withdraw money, deposit money, and transfer money.

withdraw_money() – manages withdrawals with overdraft rules and fees.

transfer_money() – allows flexible money transfers between accounts, with proper validation.

---------------------------------------------------------------------------------------------><---------------------------------------------------------------------------------------------------------------

Lessons Learned:

- Reading from and writing to CSV files for data storage.
- Organizing class methods and handling complex user input logic.
- Implementing real-world banking scenarios such as overdrafts and account validation.
- Thinking in an organized way when designing functions that interact with files and multiple user choices.

---------------------------------------------------------------------------------------------><---------------------------------------------------------------------------------------------------------------