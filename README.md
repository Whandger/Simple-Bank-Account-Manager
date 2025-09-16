# Simple Bank Account Manager
#### Video Demo: <URL HERE>
#### Description:
This project is a simple command-line Python program designed to help users manage a personal bank account balance. The program allows users to deposit money, withdraw money, and view their current account balance. All data is stored persistently in a CSV file named `balance.csv`, which ensures that the balance is maintained even after the program is closed and reopened.

The main goal of this project was to create a lightweight, easy-to-use application that introduces fundamental concepts of Python programming, file handling, and user input validation. The project demonstrates how to interact with CSV files, handle potential errors gracefully, and create a user-friendly command-line interface.

---

### Project Structure

- `main.py`: The main Python file containing all the program logic. It handles user interaction, input validation, balance management, and CSV file operations.
- `balance.csv`: The CSV file used to store the current balance. This file is automatically created when the program is first run if it does not already exist.
- `README.md`: This documentation file that explains the project, its functionality, and design choices.

---

### How the Program Works

When the program starts, it checks for the existence of the `balance.csv` file using the `initialize_csv()` function. If the file does not exist, it is created with an initial balance of 0. Otherwise, the current balance is read from the file. The main loop then begins, displaying the current balance and presenting the user with a menu of options: deposit, withdraw, or end the transaction.

- **Deposit:** The user is prompted to enter an amount to deposit. The program validates the input to ensure it is a number and then updates the balance, writing the new balance back to the CSV file.
- **Withdraw:** Similar to deposit, the user enters an amount to withdraw. The program checks that sufficient funds are available before completing the transaction. If the balance is insufficient, a friendly error message is displayed.
- **End Transaction:** Exits the program gracefully, printing a message to confirm the transaction has ended.

The `display_balance()` function formats the balance nicely and shows the current date, enhancing the readability of the information presented to the user.

---

### Design Choices

Several design decisions were made to improve usability and maintainability:

1. **CSV for Persistent Storage:** Using a CSV file allows the program to save the account balance without requiring a database. This keeps the project lightweight and simple while still providing persistence.
2. **Global Balance Variable:** A global variable for balance was used to simplify updates and ensure consistency across functions. While global variables are generally discouraged, in this small project it provides a clear and simple way to manage state.
3. **Input Validation:** Every user input is validated to prevent crashes due to invalid data. The program prints informative error messages and prompts the user to try again when incorrect input is detected.
4. **Formatted Output:** Balances are displayed with two decimal places and formatted for readability, providing a professional look in the command-line interface.

---

### Future Improvements

In the future, this project could be extended with additional features such as:

- Handling multiple accounts
- Adding a transaction history
- Supporting different currencies
- Creating a graphical user interface (GUI) for better usability

---

This project serves as a foundational example of combining Python programming, file management, and user input handling in a practical, real-world application. It demonstrates core programming concepts in a way that is both accessible and functional, making it an excellent learning tool for beginners.
