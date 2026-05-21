#Rock paper and scissors game
import random
print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]
while True:
# Get user input
    #Quit option
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    if user_choice == "quit":
        print("Thanks for playing! Goodbye!")
        break
    #Invalid user input
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    #Generate computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
#Determine the winner
    #Tie condition
    if user_choice == computer_choice:
        print("It's a tie!")
    #Winning conditions for the user
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    #Losing conditions for the user
    else:
        print("Computer wins!")
#End of the game loop, the user can play again or quit.