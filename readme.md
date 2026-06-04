# 🏦 ACME Bank System

A simple **command-line banking system** built in Python. A cashier can open new customer accounts, and customers can log in to manage their money — withdrawing, depositing, and transferring funds. All account data is stored in a CSV file (`bank.csv`), so the data persists between runs.

---

## ✨ Features

### 🧑‍💼 Cashier
- **Add new customer accounts** with full input validation:
  - Account ID — exactly 5 digits and unique.
  - First and last name — letters only.
  - Password — exactly 9 characters.
  - Opening checking and saving balances — must be numbers.

### 🧍 Customer
- **Log in** with an account ID and password and get a personalized welcome.
- **Withdraw money** from checking or saving, with full overdraft handling.
- **Deposit money** into checking or saving.
- **Transfer money** between your own accounts or to another customer's account by ID.

### 💸 Overdraft Rules
- An account can go as low as **-$100**.
- Each overdraft adds a **$35 fee**.
- After **2 overdrafts**, the account becomes **not activated** and is frozen until the fee is paid.
- The customer can pay the outstanding fee from checking or saving to **reactivate** the account.

---

## 🗂️ Project Structure

```
banking-project-main/
├── bank/
│   ├── __init__.py
│   └── acme_bank.py     # Main program: Cashier, Accounts, and Bank classes
├── test/
│   ├── __init__.py
│   └── test_acme_bank.py  # Unit tests (unittest)
├── bank.csv             # Data store for all accounts
└── readme.md
```

### The Classes
| Class | Responsibility |
|-------|----------------|
| `Cashier` | Adds and validates new customer accounts (`add_customer_account`). |
| `Accounts` | Handles login and all customer operations: `user_login`, `withdraw_money`, `deposit_money`, `transfer_money`. |
| `Bank` | The main menu loop (`menu`) that ties everything together. |

### Data Format (`bank.csv`)
Each row represents one account:

| Column | Meaning |
|--------|---------|
| `account_id` | 5-digit unique ID |
| `first_name` / `last_name` | Account holder's name |
| `password` | Account password |
| `balance_checking` | Checking account balance |
| `balance_savings` | Saving account balance |
| `account_status` | `activated` or `not_activated` |
| `overdraft_fee` | Outstanding overdraft fee owed |

---

## 🚀 Getting Started

### Prerequisites
- **Python 3** installed (no external libraries needed — uses the standard library only).

### Run the App
From the project root (the folder containing `bank.csv`):
```bash
python -m bank.acme_bank
```

You'll see the main menu:
```
---------------------------------> Welcome to the ACME Bank! <---------------------------------
SELECT A CHOICE

1- Add New Customer
2- Login Into Account
3- Exit
```

> **Note:** The app reads and writes `bank.csv` using a relative path, so run it from the project root so the file is found correctly.

### Run the Tests
```bash
python -m unittest
```

---

## 🛠️ Built With
- **Python 3** — core language
- **csv** — reading and writing account data
- **unittest** — testing

---

## 💡 Possible Improvements
- **Hash passwords** instead of storing them as plain text in the CSV (important for any real use).
- Flesh out the placeholder tests for login, deposit, withdraw, and transfer.
- Reduce duplicated logic between the checking and saving branches of `withdraw_money`.
- Add a transaction history / statement feature.
- Move from CSV to a small database (e.g. SQLite) for safer concurrent access.

---

## 📚 Lessons Learned
- Reading from and writing to CSV files for persistent storage.
- Organizing class methods and handling complex, multi-step user input.
- Implementing real-world banking scenarios like overdrafts and account validation.
- Designing functions that interact with files across many user choices.

---

*A hands-on project for learning file handling, classes, and real-world logic in Python. 💰*
