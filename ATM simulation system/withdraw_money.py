from utils import balance,record

def withdraw_money():
    money=float(input("Enter the amount of money you want to withdraw: "))
    if money>0 and money<balance[0]:
        balance[0]-=money
        record.append(f"Withdrawal:{money}")
        print(money,"rupees debited from your account!!")
    elif money>balance[0]:
        print("Insufficient balance..")
    elif money==0:
        print("Zero rupees can't be withdrawn")
    else:
        print("Enter valid amount of money!")
    print("*"*50)

