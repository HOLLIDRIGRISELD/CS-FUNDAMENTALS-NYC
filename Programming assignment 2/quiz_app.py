import requests
import json
import random
import html

#login or register
authentication = False
while not authentication:
    #opening screen
    print("WELCOME TO THE TRIVAI QUIZ GAME!")

    #authetication screen
    print("1. LOGIN")
    print("2. REGISTER")
    choice = input("CHOOSE FROM 1 or 2: ")

    #login proccess 
    if choice == "1":
        username = input("ENTER YOUR USERNAME: ")
        password = input("ENTER YOUR PASSWORD: ")

        #check is they are in  the users file
        file = open("users.txt", "r")
        users = file.readlines()

        for user in users:
            saved_username, saved_password = user.strip().split(":")
            if username == saved_username and password == saved_password:
                print("SUCCESSFUL LOGIN!")
                authentication = True
                break
        
        #message is login was wrong
        if not authentication:
            print("INVALID USERNAME OR PASSWORD. PLEASE TRY AGAIN.")

    #registation proccess
    elif choice == "2":
        username = input("CHOOSE A USERNAME: ")
        password = input("CHOOSE A PASSWORD: ")

        #check if the username already exists
        file = open("users.txt", "r")
        users = file.readlines()

        user_exist = False
        for user in users:
            if username == user.strip().split(":")[0]:
                user_exist = True
                break
            
        if user_exist:
            print("USERNAME EXITS. PLEASE TRY A DIFFERENT ONE.")
        else:
            file = open("users.txt", "a")
            file.write(f"{username}:{password}\n")
            print("REGISTRATION COMPLETE. YOU CAN NOW PROCCED")


# Main game loop
play_again = True
while play_again:

    # Get the questions from the API
    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    response = requests.get(url)
    data = response.json()
    questions = data["results"]

    score = 0
    print("THE QUIZ STARTED! ANSWER THE QUESTIONS!")

    #display each question
    for i in range(len(questions)):
        question_data = questions[i]
        question = html.unescape(question_data["question"])
        print(f"QUESTION {i + 1}: {question}")

        #deferentiate the answers 
        correct_answer = html.unescape(question_data["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in question_data["incorrect_answers"]]

        #combine them again in a list and shuffle
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)

        #show answers
        for j in range(len(answers)):
            print(f"{j + 1}. {answers[j]}")

        #get the users answer number only
        user_answer = input("YOUR ANSWER 1-4: ")
        #found the isdigit() method at https://www.youtube.com/watch?v=FvC3U8Xt-kM
        while not user_answer.isdigit() or int(user_answer) < 1 or int(user_answer) > 4:
            user_answer = input("INVALID. ENTER A NUBER FROM 1 TO 4: ")

        #check if the answer is correct
        if answers[int(user_answer) - 1] == correct_answer:
            print("CORRECT!")
            score += 1
        else:
            print(f"WRONG! THE CORRECT ANSWER WAS: {correct_answer}\n")

    #show final score of user
    print("THE QUIZ IS OVER! YOUR SCORE:",score,"/5")

    #update scores
    file = open("scores.txt", "r")
    scores = {}
    for line in file:
        parts = line.strip().split(":")
        user = parts[0]
        user_score = int(parts[1])
        scores[user] = user_score
    file.close()  # Close the file after reading

    #update or add the scores
    if username in scores:
        scores[username] += score
    else:
        scores[username] = score

    #save the updated scores to the txt
    file = open("scores.txt", "w")
    for user, user_score in scores.items():
        file.write(f"{user}:{user_score}\n")
    file.close()

    #show the user's total score
    print(f"YOUR TOTAL SCORE IS: {scores[username]}")

    #ask user if they want to play again?
    choice = input("DO YOU WANT TO PLAY AGAIN? YES or NO: ").lower()
    if choice != "yes":
        play_again = False

print("THANKS FOR PLAYING!")
