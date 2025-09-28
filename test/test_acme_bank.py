import unittest
import tempfile
import csv
import os

from  bank.acme_bank import Cashier
from  bank.acme_bank import Accounts
from  bank.acme_bank import Bank
from unittest.mock import patch

test_file = 'test_bank.csv'
test_rows = [
    ['12834', 'Jana', 'Sandeyouni', 'je9e9ei39', '5000', '3000', 'activated', '0']
]

class TestCashier(unittest.TestCase):
    
    def setUp(self):
        with open(test_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(test_rows)
            
    def tearDown(self):
        os.remove(test_file)
        
    
    def test_add_customer_account(self):
        
        with open(test_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['12834', 'Jana', 'Sandeyouni', 'je9e9ei39', '5000', '3000', 'activated', '0'])
            
        with open(test_file, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[1][1], 'Jana')
            self.assertEqual(rows[1][4], '5000')
            self.assertEqual(rows[1][5], '3000')
            
    if __name__ == "__main__":
        unittest.main()

class TestAccounts(unittest.TestCase):
    def test_user_login(self):
         pass
     
    def test_withdraw_money(self):
         pass
    
    def test_deposit_money(self):
         pass
     
    def test_transfer_money(self):
         pass
     

class TestBank(unittest.TestCase):
    def test_menu(self):
         pass