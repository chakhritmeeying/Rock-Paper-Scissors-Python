import random


choices = ["rock", "paper", "scissors"]
score = {"wins": 0, "losses": 0, "ties": 0}


def get_result(user, computer):
    # Check result
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"


def update_score(result):

    if result == "win":
        score["wins"] += 1
        print("You Win! 🎉\n")
    elif result == "lose":
        score["losses"] += 1
        print("You Lose! 😢\n")
    else:
        score["ties"] += 1
        print("It's a Tie! 🤝\n")


def show_score():
    print(
        f"Score => Wins: {score['wins']} / Losses:{score['losses']} / Ties:{score['ties']} \n")


# intro message
print("Wellcome to Rock-Paper-Scissors Game !!!")
print("Enter 'Rock' , 'Paper' or 'Scissors' to play")
print("Enter Reset to reset score")
print("Enter Exit to stop the game.")
print("Let's Start !!!")
print("------------------------------------------------\n")

# main game loop
while True:
    user = input("Your Choose : ").lower()  # User Choose

    if user == "exit":
        print("Thank to playing !! Bye")
        break
    if user == "reset":
        score = {"wins": 0, "losses": 0, "ties": 0}
        print("Score has been reset.\n")
        show_score()
        continue
    if user not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.\n")
        continue

    computer = random.choice(choices)  # Compuet Choose
    print(f"Computer Chooses : {computer}")
    update_score(get_result(user, computer))
    show_score()
