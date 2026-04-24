from  utils import books,issued_books,student_fine

def return_books():
    #gets the student name to check the fine on the book returner 
    check = input("Enter your name : ")
    #checks the fine on the student name and store that in a new variable
    for i in student_fine:
        if i ==check:
            n=student_fine[i]
    #checks if the student issued book from this library
    if check not in student_fine:
        print("You did not issue book from here..")
        return
    #main function to return the books 
    name = input("Enter the name of the book you want to return: ")
    if name in issued_books:
        books[name]="available"
        issued_books.pop(name)
        print("Book is Returned!!")
    else:
        print("Book is not issued from this library !!!")

    #tells that how much fine is on the returner
    if n==0:
        print("You have to pay full price of the book!!!")
    elif n==1:
        print("NO fine on you, Enjoy!!")
    else:
        print("Fine on you is of",n,"rs")
    print("*"*50)


