import random


def comp():
    options = ["Snake", "Water", "Gun"]
    return random.choice(options).lower()  # return the option in lower case


def user():
    choice = input("Enter your option: ").lower()
    return choice  # return the choice of user in lower case


def check(choice):
    options = ["snake", "water", "gun"]
    if (choice in options):
        return False
    else:
        return True


def winner(user_choice, comp_choice):
    if (user_choice == "snake"):
        if (comp_choice == "snake"):
            print("Its a Draw")
        elif (comp_choice == "gun"):
            print("You lose")
        else:
            print("You Win")
    elif (user_choice == "gun"):
        if (comp_choice == "snake"):
            print("You Win")
        elif (comp_choice == "gun"):
            print("Its a draw")
        else:
            print("You Lose")
    elif (user_choice == "water"):
        if (comp_choice == "snake"):
            print("You Lose")
        elif (comp_choice == "gun"):
            print("YOu Win")
        else:
            print("Its a draw")
    print(f"You Choose: {user_choice} and Computer Choose: {comp_choice}")


def main():
    print("Type your option from Snake, Water, Gun \n Make sure the spellings are correct Type Exit to Quit the game")
    game = True
    while game:
        choice = user()
        if (choice == "exit"):
            game = False
            print("THank TOu For PLaying HTe Game")
        elif (check(choice)):
            print("Invalid choice")
            continue
        else:
            comp_choice = comp()
            winner(choice, comp_choice)


main()
