#Ask user for a word and find how many times the word exists in the story.txt
#file.

#read the text
file = open('week_07_story.txt')
lines = file.readlines()

word = input("Give me a word :")
counter = 0


# for each line
for line in lines:
    # split the line into words 
    words = line.split()
    counter += words.count(word)

# print the counter
print(counter)

#if in any case the error "FileNotFoundError: [Errno 2] No such file or directory: 'week_07_story.txt'":
#please go to the terminal and make sure you are in the right directory.  "...\CS-FUNDAMENTALS-NYC\Homework"