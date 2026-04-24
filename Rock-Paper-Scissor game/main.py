from stone import stone
from paper import paper
from scissor import scissor

def game():
    while True:
        print("-"*20,"MENU","-"*20)
        print("\n1.Stone")
        print("2.Paper")
        print("3.Scissor")
        print("4.Exit")

        choice = int(input("Enter your choice: "))

        if choice==1:
            stone()
        elif choice==2:
            paper()
        elif choice==3:
            scissor()
        elif choice==4:
            print("Thank You!!")
            break
        else:
            print("Kindly enter a valid choice!!")
            break
    print("*"*50)

game()