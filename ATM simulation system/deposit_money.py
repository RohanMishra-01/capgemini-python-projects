from utils import balance,record

def deposit_money():
    money =float(input("Enter the amount of money to deposit: "))
    if money>0:
        balance[0]+=money
        record.append(f"Amount credited: {money}")
        print(money," rupees Credited to your account!!")
    elif money==0:
        print("Zero rupees can't be credited!!")
    else:
        print("Enter valid amount of money !!")
    print("*"*50)
