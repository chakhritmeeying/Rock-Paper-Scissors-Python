import random


def result(user, computer):
    # Check result
    if user == computer:
        return print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return print("You win!\n")
    else:
        return print("You lose!\n")


choices = ["rock", "paper", "scissors"]
print("Wellcome to Rock-Paper-Scissors Game !!!")
print("Enter 'Rock' , 'Paper' or 'Scissors' to play")
print("Enter Exit to stop the game. \n")

while True:
    user = input("Your Choose : ").lower()  # User Choose

    if user == "exit":
        print("Thank to playing !! Bye")
        break
    if user not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.\n")
        continue
    computer = random.choice(choices)  # Compuet Choose
    print(f"Computer Chooses : {computer}")
    result(user, computer)
