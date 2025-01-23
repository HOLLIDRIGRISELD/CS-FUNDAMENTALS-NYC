#Use the users CSV data below and put them in a file users.csv.
#Then, write a program to ask user for username and pin. If the username and pin are in the file,
#respond with a welcome message, else display a user not found message.

# Open and read the CSV file
file = open('week_07_userdata.csv')
lines = file.readlines()

# Ask for username and PIN
username = input("Enter username: ")
pin = input("Enter PIN: ")

# Check if the username and PIN match in the csv
flag = False
for i in range(1, len(lines)):
    line = lines[i].strip()
    parts = line.split(',')
    if parts[0] == username and parts[1] == pin:
        flag = True
        first = parts[2]
        last = parts[3]
        break

# Output the result
if flag:
    print("Welcome",first,last,"!")
else:
    print("User not found or incorrect PIN.")

#if in any case of the error "FileNotFoundError: [Errno 2] No such file or directory: 'week_07_userdata.csv'":
#please go to the terminal and make sure you are in the right directory.  "...\CS-FUNDAMENTALS-NYC\Homework"