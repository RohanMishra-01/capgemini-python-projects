from computer_choice import computer_choice


def stone():
    move = computer_choice()
    if move=="stone":
        print("\nUser choice: Stone")
        print("Computer Choice: Stone")
        print("\nResult: Its a draw!!")
    elif move=="paper":
        print("\nUser choice: Stone")
        print("Computer Choice: Paper")
        print("\nResult: Computer won!!")
    else:
        print("\nUser choice: Stone")
        print("Computer Choice: Scissor")
        print("\nResult: You Won!!")
    print("*"*50)
