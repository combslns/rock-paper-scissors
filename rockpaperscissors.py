import random

score = [0,0,0]
Win = 0
Lose = 0
Tie = 0
game = True

while game:
    user_input = input("Rock? Paper? or Scissors?")
    game_options = ["rock", "paper", "scissors"]
    rock_problem = ["paper", "Paper", 'Scissors', 'scissors']
    paper_problem = ["rock", 'Rock', "Scissors", 'scissors']
    scissors_problem = ["Rock", 'Rock', "Paper", "paper"]
    result = ['Win', 'Lose', 'Tie']
    all_choices = ['rock', 'Rock', 'Paper', 'paper', 'Scissors', 'scissors']
    game_choice = random.choice(game_options)

    if user_input not in all_choices:
        print('Not A Valid Input!')
        continue

    print(f"\nYou chose {user_input}, computer chose {game_choice}.\n")

    if user_input == game_choice:
        print(f"Both players selected {user_input}. It's a tie!")
        outcome = result[2]
    elif user_input not in rock_problem:
        if game_choice == "scissors":
            print("Rock smashes scissors! You win!")
            outcome = result[0]
        else:
            print("Paper covers rock! You lose.")
            outcome = result[1]
    elif user_input not in paper_problem:
        if game_choice == "rock":
            print("Paper covers rock! You win!")
            outcome = result[0]
        else:
            print("Scissors cuts paper! You lose.")
            outcome = result[1] 
    elif user_input not in scissors_problem:
        if game_choice == "paper":
            print("Scissors cuts paper! You win!")
            outcome = result[0]
        else:
            print("Rock smashes scissors! You lose.")
            outcome = result[1]

    if outcome == result[0]:
        score[0] += 1
    elif outcome == result[1]:
        score[1] += 1
    elif outcome == result[2]:
        score[2] += 1
    
    print("Score: " + str(score[0]) + " - " + str(score[1]) + " - " + str(score[2]) + "\n")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != 'yes':
        game = False