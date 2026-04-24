#imported all functions from different files
from add_book import add_books
from show_book import show_books
from issue_books import issue_book
from return_book import return_books


#main body---------------------------------------
def library():
    while True:
        print("\n--------------------MENU-------------------- ")
        print("Choose your choice:- ")
        print("\n1. Add book in the library")
        print("2. Show books in the library")
        print("3. Issue books from the library")
        print("4. Return book to the library")
        print("5. Exit from the library ")
        print("*"*50)
        
        choice = int(input("\nEnter your choice: "))

        if choice==1:
            add_books()
        elif choice==2:
            show_books()
        elif choice==3:
            issue_book()
        elif choice==4:
            return_books()
        elif choice==5:
            print("Thank You!!!")
            print("Please visit again!!")
            break
        else:
            print("Please enter a valid choice!!!!")
            break

#function call-----------------------------
library()