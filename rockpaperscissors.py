import random
def get_computer_choice():
    options=["rock","paper","scissors"]
    computer_pick = random.choice(options)
    return computer_pick
def get_user_choice():
    while True:
        user_pick=input("please type Rock,paper,or scissors:").lower()
        if user_pick in ["rock", "paper", "scissors"]:
            return user_pick
        else:
            print("that's not a valid choice. Try again!")
def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or\
         (user == "scissors" and computer == "paper") or\
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
def play_game():
    user_score=0
    computer_score=0
    print("welcome to the rock-paper-scissors game!")
    while True:
        print("\n new round!")
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        print(f"\nyou chose:{user_choice.capitalize()}")
        print(f"computer chose:{computer_choice.capitalize()}")
        winner=decide_winner(user_choice,computer_choice)
        if winner == "tie":
            print("it's a tie this round!")
        elif winner == "user":
            print("you win this round!")
            user_score+=1
        else:
            print("computer wins this round!")
            computer_score+=1
        print(f"\n scoreboard you:{user_score} | computer:{computer_score}")
        play_again=input("\n do you want to play another round? (yes/no):").lower()
        if play_again!="yes":
            print("\n thanks for playing! here's the final score:")
            print(f"you:{user_score} | computer:{computer_score}")
            print("see you next time!")
            break
if __name__ == "__main__" : 
    play_game()
            
