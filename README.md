# Simple Bank Account Manager

#### Video Demo: <URL HERE>

#### Description:

This project is a simple command-line Python program designed to help users manage a personal bank account balance. In this new version, the program supports **multiple accounts**: each user is identified by a **4-digit code** and associated with a personal balance file. The program allows users to deposit money, withdraw money, and view their account balance. All data is stored persistently in CSV files, ensuring that balances are maintained even after the program is closed and reopened.

The main goal of this project was to create a lightweight, easy-to-use application that introduces fundamental concepts of Python programming, file handling, user input validation, and basic account management. The project demonstrates how to interact with CSV files, handle potential errors gracefully, and create a user-friendly command-line interface.

---

### Project Structure

* `main.py`: The main Python file containing all the program logic. It handles user interaction, input validation, balance management, account creation/login, and CSV file operations.
* `<id_code>.csv`: A CSV file that stores the account owner’s **name** and **ID code** (created when a new 4-digit code is registered).
* `balance_<id_code>.csv`: A CSV file that stores the current balance for that account. This file is automatically created when the account is initialized and updated after each transaction.
* `README.md`: This documentation file that explains the project, its functionality, and design choices.

---

### How the Program Works

When the program starts, it calls the `account()` function to request a **4-digit code** from the user. If the code does not exist, the user is prompted for a first name and a new account file `<id_code>.csv` is created. If the code exists, the program reads the stored owner name and continues.

1. **Account Creation / Login (`account()`):**

   * Prompts for a 4-digit ID code.
   * If the code is new, asks for the user's first name and writes a `<id_code>.csv` file with that information.
   * If the code exists, reads the owner name from `<id_code>.csv` and returns it.

2. **Balance Initialization (`initialize_csv()`):**

   * Uses a file named `balance_<id_code>.csv` to keep the account balance.
   * If it doesn’t exist, creates it with an initial balance of 0.
   * Otherwise, reads the current balance and returns it to the program.

3. **Main Menu:**

   * **Deposit:** User enters a value to deposit; the program validates the input, updates the in-memory balance, and persists it with `write_csv()`.
   * **Withdraw:** User enters a value to withdraw; the program checks for sufficient funds before updating and persisting the balance.
   * **End Transaction:** Exits the program gracefully.

4. **Formatted Output:**
   The `display_balance()` function formats the balance with two decimal places and shows the current date for clarity.

---

### Design Choices

1. **Multiple Accounts Support:** By linking each user to a unique 4-digit ID, the system supports multiple independent accounts stored as separate files.
2. **Separation of User Data and Balances:** Two CSV files are used per account:

   * `<id_code>.csv` → stores account owner’s name and ID.
   * `balance_<id_code>.csv` → stores the numeric balance.
3. **Input Validation:** The program validates every user input (numeric checks for ID and amounts, command choices) and displays friendly error messages using a centralized `message()` function.
4. **Simplicity & Persistence:** Using CSV files keeps the project lightweight while providing persistent storage without a database.

---

### Future Improvements

Potential enhancements for future versions:

* Adding transaction history per account
* Implementing password protection or PIN system for accounts
* Supporting different currencies
* Creating a graphical interface (GUI or web-based) for better usability
* Adding account deletion and management features

---

This project now demonstrates not only file handling and user input but also **basic account management for multiple users**, making it a more realistic example of how small-scale banking systems work.
