import os
from project import deposit, withdraw, message

def test_deposit():
    global balance
    balance = 100
    deposit(50)
    assert balance == 150

def test_withdraw():
    global balance
    balance = 200
    withdraw(80)
    assert balance == 120
    

    withdraw(200)
    assert balance == 120 

def test_message():
    assert "Use right commands" in message(1)
    assert "Insufficient funds" in message(2)
    assert "Transaction Ended" in message(3)