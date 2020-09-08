import random

# PROCEDURE
def show_welcome():
    print(welcome_message)

def get_history():
    text_file = open("history.txt", "r")
    text_data = text_file.read().split(",")
    text_file.close()
    return {
        "wins": int(text_data[0]),
        "ties": int(text_data[1]),
        "losses": int(text_data[2])
    }

def show_history():
    print(history_message %(score["wins"], score["ties"], score["losses"]))

def user_choice():
    choice = input("[1] rock [2] paper [3] scissors [9] quit\n")
    return choice_options[int(choice)]

def quit_game(wins, ties, losses):
    text_file = open("history.txt", "w")
    text_file.write(str(wins) + "," + str(ties) + "," + str(losses))
    text_file.close()

def compare_choices(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"

def display_message_update_score(result):
    if result == "tie":
        print(tie_message)
        score["ties"] +=1
    elif result == "win":
        print(win_message)
        score["wins"] +=1
    else:
        print(lose_message)
        score["losses"] +=1

# variables

welcome_message = "Welcome to Rock, Papers, Scissors!"
history_message = "Wins: %s, Ties: %s, Losses: %s"
quit_message = "Thanks for playing, come back anytime"
win_message = "Nice, you won that one"
lose_message = "Ouch, did that hurt?"
tie_message = "TIE"

score = {
    "wins": 0,
    "ties": 0,
    "losses": 0
}

history = get_history()
score["wins"] = history["wins"] 
score["ties"] = history["ties"] 
score["losses"] = history["losses"]

choice_options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    9: "quit"
}


# GAME 

show_welcome()
show_history()

user_play = user_choice()

while user_choice != "quit":
    computer_choice = choice_options[random.randint(1,3)]
    result = compare_choices(user_choice, computer_choice)
    display_message_update_score(result)
    user_play = user_choice()

quit_game(score["wins"], score["ties"], score["losses"])