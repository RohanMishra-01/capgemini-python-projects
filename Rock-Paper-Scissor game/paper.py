from computer_choice import computer_choice


def paper():
    move = computer_choice()
    if move=="stone":
        print("\nUser choice: Paper")
        print("Computer Choice: Stone")
        print("\nResult: You won !!")
    elif move=="paper":
        print("\nUser choice: Paper")
        print("Computer Choice: Paper")
        print("\nResult: It is a Tie!!")
    else:
        print("\nUser choice: Paper")
        print("Computer Choice: Scissor")
        print("\nResult: Computer Won!!")
    print("*"*50)
