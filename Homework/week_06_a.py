#Given a list of students, generate usernames for each one of them and put
#them in another list. In case a username already exists, due to name similarity, use a counter to
#add a number at the end and increase the counter.
#Example:
#students = [‘John Doe’, ‘Mary Smith’, ‘Andrew Green’, ‘Lisa Tomas’,‘Mike Smith’, ‘Alex Green’]
#result will be => [‘jdoe’, ‘msmith’, ‘agreen’, ‘ltomas’, ‘msmith1’,‘agreen2’]

students = ['John Doe', 'Mary Smith', 'Andrew Green', 'Lisa Tomas', 'Mike Smith', 'Alex Green']
usernames = []

#start of creation of usernames
for student in students:  

    #spliting of list and creation of the base username
    first,last = student.split() 
    basename = first[0].lower() + last.lower()
    username = basename
    
   #check is the basename is already in the usernames
   #if yes add a counter 
    counter = 1
    while username in usernames:
        username = basename + str(counter)
        counter += 1
    

    usernames.append(username)

print(usernames)
