
import random

def play_game():
    wins_user = 0
    wins_computer = 0
    attempts = 6
    
    while attempts > 0:
        user_choice = input("Choose rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        if user_choice == "rock":
            if computer_choice == "rock":
                print("Computer chose rock. It's a tie!")
            elif computer_choice == "paper":
                print("Computer chose paper. Computer wins!")
                wins_computer += 1
            else:
                print("Computer chose scissors. You win!")
                wins_user += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Computer chose rock. You win!")
                wins_user += 1
            elif computer_choice == "paper":
                print("Computer chose paper. It's a tie!")
            else:
                print("Computer chose scissors. Computer wins!")
                wins_computer += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer chose rock. Computer wins!")
                wins_computer += 1
            elif computer_choice == "paper":
                print("Computer chose paper. You win!")
                wins_user += 1
            else:
                print("Computer chose scissors. It's a tie!")
        
        attempts -= 1
    
    print("Game over!")
    print("User wins:", wins_user)
    print("Computer wins:", wins_computer)

play_game()