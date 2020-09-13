from abc import ABCMeta, abstractmethod
from random import randint
import pyinputplus  # This will help me with input prompts as this app uses many


class Account(metaclass=ABCMeta):
    """Abstract class that forces derived class to have same methods (all Account class should have this methods)"""

    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount:

    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        """So account looks like this: 55555 = 'Lukasz' 10000, where 55555 is acc number, Lukasz is name,
        and 1000 is initial deposit (dict: [key][0] => name; [key][1] => balance"""
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        return print("Your account number is: {}".format(self.accountNumber))

    def authenticate(self, name, accountNumber):
        """Check if in dict.keys() there is given accNum if there is check if given name matches that accNum"""
        if accountNumber in self.savingsAccounts.keys():
            if name in self.savingsAccounts[accountNumber][0] == name:
                print("Authentication Successful!")
                self.accountNumber = accountNumber
                return True
            else:
                # I could tell user that given name is wrong but i want it to be more secure by not providing this inf
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def displayBalance(self):
        return print("Available balance:", self.savingsAccounts[self.accountNumber][1])

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Sorry, insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal successful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit successful.")
        self.displayBalance()


mainMenu = "\nEnter 1 to create account\n" \
           "Enter 2 to log in\n" \
           "Enter 3 to exit\n" \
           "Your choice: "

accountMenu = "\nEnter 1 to display balance\n" \
              "Enter 2 to withdraw\n" \
              "Enter 3 to deposit\n" \
              "Enter 4 to go to main menu\n" \
              "Enter 5 to exit\n" \
              "Your choice: "

savingacc1 = SavingsAccount()


def main():
    while (user_input := input(mainMenu)) != "3":
        if user_input == "1":
            name = input("Enter your name: ").strip()
            deposit = pyinputplus.inputNum("Enter your initial deposit: ")
            savingacc1.createAccount(name, deposit)
        elif user_input == "2":
            name = input("Enter your name: ").strip()
            accountNumber = pyinputplus.inputNum("Enter your account number: ")
            if savingacc1.authenticate(name, accountNumber):
                while (user_input := input(accountMenu)) != "4":
                    if user_input == "1":
                        savingacc1.displayBalance()
                    elif user_input == "2":
                        amount = pyinputplus.inputNum("Enter withdrawal amount: ")
                        savingacc1.withdraw(amount)
                    elif user_input == "3":
                        amount = pyinputplus.inputNum("Enter deposit amount: ")
                        savingacc1.deposit(amount)
                    elif user_input == "5":
                        return

        else:
            print("Wrong input! Please enter number 1-3")


main()
