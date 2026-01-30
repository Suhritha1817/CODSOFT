import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("User choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("Result: It's a tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("Result: You win")
    else:
        print("Result: You lose")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Game ended.")
        break
