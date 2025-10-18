from datetime import datetime
class BankAccount:
     
    def __init__(self, account_holder:str, initial_balance:int=0):
        self.__account_holder= account_holder
        self.__balance= initial_balance

    def set_account_holder(self, account_holder:str):
        try:
            if not account_holder.isalpha():
                raise Exception("The account holder name should only be letters!")
        except Exception as e:
            print(e)

    def get_account_holder(self):
        return self.__account_holder
    
    def set_balance(self, initial_balance:int):
        try:
            if initial_balance<0:
                raise Exception("The initiail balance should not be less than zero!")
        except Exception as e:
            print(e)

    def get_balance(self):
        return self.__balance


    def deposit(self,amount:int):
        try:
            self.__balance+=amount
            if amount<=0:
                raise Exception("The deposit amount should be more than zero!")
        except Exception as e:
            print(e)

        return f"The account balance is: {self.get_balance()}\nTransaction done successfuly in: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    
    def withdraw(self, amount:int):
        try:
        
            if amount<=0:
                raise Exception("The deposit amount should be more than zero!")

            if self.__balance< amount:
                raise Exception("Unsuccessful transaction!\nThe amount you are tying to withdraw is greater than your currnt balance.")
            self.__balance-=amount

        except Exception as e:
            print(e)
        
        return f"The account balance is: {self.get_balance()}\nTransaction done successfuly in: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"

    def display_balance(self):
        return self.get_balance()

    def display_account_holder(self):
        return self.get_account_holder()

