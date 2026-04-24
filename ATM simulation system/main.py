from deposit_money import deposit_money
from withdraw_money import withdraw_money
from display_money import display_money
from bank_statement import bank_statement



def atm():
    while True:
        print("-"*20,"MENU","-"*20)
        print("\nChoose your choice: ")
        print("1.Deposit Money")
        print("2.Withdraw Money")
        print("3.Display Money")
        print("4.Bank statement")
        print("5.Exit")
        print("-"*50)

        choice = int(input("Enter your choice: "))

        if choice==1:
            deposit_money()
        elif choice ==2:
            withdraw_money()
        elif choice==3:
            display_money()
        elif choice==4:
            bank_statement()
        elif choice==5:
            print("Thank you!!")
            print("Kindly Visit Again!!")
            break
        else:
            print("Please enter a valid choice !!")

atm()