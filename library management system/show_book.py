from utils import books
def show_books():
    if len(books)==0:    #Checks whether a book is present in the library or not 
        print("No books available!!")
    else:
        print("\nBooks available are: ")
        for book in books:
            print("\n",book)
    print("*"*50)