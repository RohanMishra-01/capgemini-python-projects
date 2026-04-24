from utils import record

def bank_statement():
    print("Transaction records are: ")
    for i in range(len(record)):
        print(record[i])
    print("Thank You!!")
    print("*"*50)
