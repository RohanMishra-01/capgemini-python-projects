from computer_choice import computer_choice


def scissor():
    move = computer_choice()
    if move=="stone":
        print("\nUser choice: Scissor")
        print("Computer Choice: Stone")
        print("\nResult: Computer Won!!")
    elif move=="paper":
        print("\nUser choice: Scissor")
        print("Computer Choice: Paper")
        print("\nResult: You won!!")
    else:
        print("\nUser choice: Scissor")
        print("Computer Choice: Scissor")
        print("\nResult: It is a Tie!!")
    print("*"*50)
