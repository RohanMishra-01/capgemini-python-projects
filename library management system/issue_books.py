from utils import books,issued_books,student_data,student_fine
from show_book import show_books


def issue_book():
    #Displays the available books in the library
    show_books()  

    #Tells about the allowed days and fine structure 
    print("Allowed days to issue a book = 7 days")
    print("\nCHARGES ON THE BOOK APPLY AS FOLLOWS: ")
    print("For more than 1 WEEK = 10rs/day/book")
    print("For more than 2 WEEK = 20rs/day/book")
    print("For more than 3 WEEK = you have to pay the full price of the book")


    #Thecks if books are available or not 
    if len(books)==0:
        print("\nNo books Available !!")
        return
    
    else:
        student_name=input("\nEnter your name : ")
        name = input("Enter name of the book you want to issue: ")
        days =int(input("Enter the number of days you want to issue the book: ")) 
        date=input("Enter date of issue (dd-mm-yyyy): ")
        student_data[student_name]= {"date":date,"days":days}   #stores student data in a dictionary 
        

    #To calculate fine and store that fine for every student individually
        extra_days=days-7
        fine=0
        if extra_days<=0:
            fine=1
        elif extra_days<=7:
            fine=extra_days*10
        elif extra_days<=14 and extra_days>7:
            fine = 7*10+ (extra_days-7)*20
        elif extra_days<=21 and extra_days>14:
            fine = 7*10+7*20+(extra_days-14)*60
        else:
            fine=0
        
    #Stores fine on each student in the form of dictionary 
        student_fine[student_name]=fine

    #Actual issuing function
        if name in books:
            books.pop(name)
            issued_books[name]="issued"
            print("\nBook is issued.")
            print("Thank you!")
        
        else:
            print("Book not available.")
            print("Thank you")
    print("*"*50)


