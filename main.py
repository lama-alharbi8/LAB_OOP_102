from Lab import BankAccount

menu= '''
Welcome to Tuwaiq Bank!
How can we help you today?

        1- To create a new account please type 'create'
        2- To make a deposit please type 'deposit'
        3- To make a withdraw please type 'withdraw'
        4- To check the account balance please type 'balance'
        5- To check the account holder name please type 'name'
        6- To exit the program please type 'exit'
'''

second_menu=  '''
Is there anything else we can help you with?

        1- To create a new account please type 'create'
        2- To make a deposit please type 'deposit'
        3- To make a withdraw please type 'withdraw'
        4- To check the account balance please type 'balance'
        5- To check the account holder name please type 'name'
        6- To exit the program please type 'exit'
'''
print(menu)

while True:
    service= input("---> ").lower()    



    if service == "create":
        try:
            account_holder= input("Please enter the account holder name: \n")
            initial_balance= int(input("\nPlease enter the initial balance: \n"))
            account= BankAccount(account_holder, initial_balance)

            if not account_holder.isalpha():
                raise Exception("The account holder name should be only letters!")

            if initial_balance<0:
                raise Exception("The initial balance should be greater than zero!")
        except Exception as e:
            print(e)

        input("")
        print(second_menu)

    elif service == "deposit":
        amount= int(input("Plese enter the amount you want to deposit: \n"))
        print(account.deposit(amount))
        input("")
        print(second_menu)


    elif service == "withdraw":
        amount= int(input("Plese enter the amount you want to withdraw: \n"))
        print(account.withdraw(amount))
        input("")
        print(second_menu)

    elif service == "balance":
        print(f"The account balance is: {account.display_balance()}")
        input("")
        print(second_menu)

    elif service == "name":
        print(f"The account holder name is: {account.display_account_holder()}")
        input("")
        print(second_menu)

    elif service == "exit":
        print("Thank you for using Tuwaiq Bank, we can't wait to see you again!")
        break
