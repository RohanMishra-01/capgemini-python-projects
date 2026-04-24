from utils import books

def add_books():
    
    while True:
        name = input("Enter book name (or enter 'exit' to stop): ")
        if name.lower()== 'exit':
            if len(books)==0:
                print("\nNo books added")
                print("Thank you!!")
                print("*"*50)
            else:
                print("\nBooks added")
                print("Thank you!!")
                print("*"*50)
            break
        else:
            books[name]="available"

