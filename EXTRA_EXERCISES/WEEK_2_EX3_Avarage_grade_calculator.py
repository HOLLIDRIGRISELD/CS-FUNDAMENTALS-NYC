answer = "yes"
i = 0
total = 0

while answer == "yes":
    Grade = input("give me your grade :")
    i = i + 1
    total = total + int(Grade)

    answer = input('do you want to continue? yes/no ?')

avarage = int(total)/i

print("Your avarage Grade is : " ,avarage)

print("made by seldi Hollidri")