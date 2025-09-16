import csv
import os
from datetime import date

balance = 0

def main():
        global balance
        balance = initialize_csv()
        today = date.today().strftime("%d/%m/%Y")
        while True:
            print(display_balance(balance, today))

            try:
                choice = int(input("1: to deposit \n2: to withdraw \n3: End Transaction\n"))
            except ValueError:
                print(message(1))
                continue
            if not choice in [1,2,3]:
                print(message(1))
                continue


            if choice == 1:
                try:
                    n = float(input("What value to deposit: "))
                except ValueError:
                    print(message(1))
                    continue
                deposit(n)
                balance = write_csv(balance)

            if choice == 2:
                try:
                    n = float(input("What value to withdraw: "))
                except ValueError:
                    print(message(1))
                    continue
                withdraw(n)
                balance = write_csv(balance)

            if choice == 3:
                print(message(3))
                break
            else:
                continue


def initialize_csv():
    filename = "balance.csv"
    
    if not os.path.exists(filename):

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["balance"])
            writer.writeheader()
            writer.writerow({"balance": 0})
        return 0 
    
    else:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                return float(row["balance"])
        return 0            


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    if n > balance:
         print(message(2))
    else:
        balance -= n


def write_csv(value):
    with open("balance.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["balance"])
        writer.writeheader()
        writer.writerow({"balance": value})
    return value


def display_balance(balance, today):
    return f"---------------------\nYour account balance\n     R${balance:8,.2f}\n     {today}\n---------------------"


def message(code):
    messages = {
        1: "---------------------\nUse right commands!\n---------------------",
        2: "---------------------\nInsufficient funds!\n---------------------",
        3: "---------------------\nTransaction Ended\n---------------------",
        4: "---------------------\nInvalid option!\n---------------------"
    }
    return messages.get(code, "---------------------")


if __name__ == "__main__":
    main()