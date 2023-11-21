#!/bin/python


# Create a class, BankAccount, for a bank account with attributes: user name, password, and
# account balance. The account balance will default to $0 if no initial value is provided. The
# BankAccount class should include three methods: withdraw, deposit, as well as account_info
# that prints account info and balance. All methods must require the correct password and print
# an error message if the password is incorrect.

import hashlib


def GetHash(input):
    m = hashlib.sha256(input.encode())
    return m.hexdigest()


class BankAccount:
    username=""
    password=""
    balance=0.0
    def __init__(self,username,password):
        self.username=username
        self.password=GetHash(password)
    def withdraw(self,ammount):
        if not self.verify():
            return 
        if self.balance<=ammount:
            print("Insufficient funds")
            return
        self.balance-=ammount
    def deposit(self,ammount):
        if not self.verify():
            return
        self.balance+=ammount
    def account_info(self):
        print("_________________________")
        print("Account for ",self.username)
        print("Hashed Password:",self.password)
        print("Account Balance:",self.balance)
        print("_________________________")
    def verify(self):
        # name=input("Enter Username:")
        # if name != self.username:
        #     print("Incorrect name")
        #     return False
        pw=input("enter password:")
        if self.password!=GetHash(pw):
            print("Incorrect Password")
            return False
        return True
        

if __name__=="__main__":

    account=BankAccount("chad","password")
    account.account_info()

    account.deposit(100)
    account.account_info()
    account.withdraw(200)
    account.withdraw(50)
    account.account_info()




