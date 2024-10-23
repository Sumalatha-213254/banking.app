from random import choice


class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. new balance is ${self.balance}.")

    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance -= amount
            print(f"withdraw ${amount}. New Balance is ${self.balance}")
        else:
            print(" Insufficient Balance!")

    def transfer(self, amount, other_account=None):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred ${amount} to other account{other_account.account_number}.")
            print(f"your new balance is ${self.balance}.")

        else:
            print(" Insufficient Balance!")
    def check_balance(self):
        print(f"your current balance is ${self.balance}.")

    def check_intrest_rate(self):
        if self.balance < 25000:
            rate = 0.05

        elif self.balance < 100000:
            rate = 0.06

        else:
            rate = 0.10
        print(f" your intrest rate is {rate*100}% based on your balance.")

    def future_value(self, year):
        rate = 0.07
        future_value = self.balance*((1+rate)**year)
        print(f" the value of your inverstiment after {year} years is ${future_value:.2f}.")

class OnlineBankingApp:
    def __init__ (self):
        self.accounts = None
        self.accounts = None
        self.accounts = {}

    def create_account(self, account_number, pin):
        if account_number not in self.acounts:
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("account created sucessfully")

        else:
            print(" account already exits")

    def login(self, account_number, pin):
        account = self.account.get (account_number)
        if account and account.pin == pin:
            print('login sucess')
            return account
        else:
            print("Invalid Pin")
            return None

    def forget_pin(self, account_number, new_pin):
        account = self.account.get (account_number)
        if account:
            account.pin = new_pin
            print(" Pin reset sucessfull!")

        else:
            print(" Account not exit")

    def forgot_pin(self, account_number, new_pin):
        pass


def main(action=None):
    app = OnlineBankingApp()

    while True:

        print(" 1. Create Account")
        print(" 2. login")
        print(" 3. Forget pin")
        print(" 4. Exit")

        input(" Select a option:")

        if choice == '1':
            account_number = input(" Enter Account Number")
            pin = input("set yur pin")
            app. create_account(account_number, pin)

        elif choice == '2':
            account_number = input(" Enter your account number:")
            pin = input(" enter your pin:")
            account = app.login(account_number, pin)

            if account:
                while True:
                    print(" 1. deposit")
                    print(" 2. withdraw")
                    print(" 3. Transfer")
                    print(" 4. check balance")
                    print(" 5. check interset rate")
                    print("6. future Value of inverstiments:")
                    print(" 7. logout")

                    if action == '1':
                        amount = float(input(" enter your amount:"))
                        account.deposit(amount)

                    elif action == '2':
                        amount = float(input(" enter your amount:"))
                        account.withdraw(amount)

                    elif action == '3':
                        to_account_number= input("Enter account_number:")
                        to_account = app.accounts. get(to_account_number)
                        if to_account:
                            amount = float(input("enter ammount to transfer:"))
                            account.transfer (to_account, amount)

                        else:
                            print(" account number invalid")
                    elif action == '4':
                        account.check_balance()

                    elif action == '5':
                        account.check_interst_rate()

                    elif action == '6':
                        int(input(" how many years:"))
                        account.future_value()

                    elif action == '7':
                        print(" logout sucess")
                        break

                    else:
                        print("Invalid selection")


        elif choice =='3':
            account_number = input("Enter your account number:")
            new_pin = input("Enter new pin:")
            app.forgot_pin(account_number, new_pin)

        elif choice =='4':
            print("Thank you")
            break

        else:
            print("Invalid selection!:")

    if __name__ == " __main__":
        main()


