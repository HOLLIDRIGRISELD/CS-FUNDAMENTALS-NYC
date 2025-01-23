#Write a program to generate random passwords. A password must be 10
#characters long and contain upper- and lower-case letters, digits 0-9, and special characters.
#Suggestion: use four lists, lower_case_letters, upper_case_letters, digits, special_characters,
#and randomly select a list and then randomly characters from the list

import random
#lists for all character types
lowercase = ["a","b","c","d","e","f",'g','h','j','k','l','m','n','o','p','q','w','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
chars = ['!','@','#','$','%','^','&','*','(',')']

# make a list that consists of all charctars to fill the rest of the password
all_chars = lowercase + upper + numbers + chars

# fisrt four digits in order to have at list one of all character types
password = [
    random.choice(lowercase),
    random.choice(upper),
    random.choice(numbers),
    random.choice(chars)
]


#create a loop to fill the rest chars
for i in range(6):
    tempword = random.choice(all_chars)
    password += tempword

#randomize the characters of the password
random.shuffle(password)

#make the password into a single sting
final_password = ""
for i in password:
    final_password += i

print('Here is a random password :',final_password)