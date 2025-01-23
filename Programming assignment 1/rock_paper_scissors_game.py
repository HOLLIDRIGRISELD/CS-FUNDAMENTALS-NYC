import random
import datetime

#start menu and username inputs
print("--WELLCOME TO ROCK-PAPER-SCISSORS--")
username = input("ENTER YOUR USERNAME : ")

#score counters and other viable options like rock paper etc.
user_score = 0
pc_score = 0

option_list = ["rock", "paper", "scissors"]

#while loop in order for the game to work until user or pc wins
while user_score < 10 and pc_score < 10:
    print("CHOOSE YOUR OPTION FROM : rock , paper or scissors")
    user_option= input("YOUR CHOICE : ")

    #in case of missinput loop in order to retype (not in )
    while user_option not in option_list:
        print("INVALID CHOICE: MAYBE YOU MISSPELLED? PLEASE TRY AGAIN!")
        user_option= input("YOUR CHOICE : ")
        print()                                                
    
    #to give the pc a choice we do a random chose for option list with
    #a tutorial i found online for https://www.youtube.com/watch?v=lCA7Fhgx8g4
    pc_option = random.choice(option_list)
    print("THE COMPUTER CHOSE : ",  pc_option)
    print()

    #check for tie
    if user_option == pc_option:
        print("--IT IS A TIE--")
    #check if player or pc wins and add score
    elif (user_option == "rock" and pc_option == "scissors") or (user_option == "paper" and pc_option == "rock") or (user_option == "scissors" and pc_option == "paper"):
        user_score += 1
        print("--YOU WON THIS ROUND--")
    else:
        pc_score += 1
        print("--THE COMPUTER WON THIS ROUND--")

    #output the rounds stats
    print("YOUR SCORE IS : ",user_score)
    print("THE COMPUTER'S SCORE IS : ",pc_score )

#check who won the game (player or pc)
if user_score == 10:
    print("CONGRATS!! YOU WON THIS GAME!!")
else:
    print("THE COMPUTER WON THIS GAME! TRY HARDER NEXT TIME!!!")



#create the score.txt file that will contain username,time,user_score,pc_score
with open("scores.txt", "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{username},{timestamp},{user_score},{pc_score}\n")

print("Your score has been saved!")



