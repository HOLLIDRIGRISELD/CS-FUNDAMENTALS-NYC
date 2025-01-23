#Create a list and fill with 20 random numbers (1 – 100).
#Then count how many of them are even.

import random

data = []
j = 0

#via random we fill a list
for i in range(20):
    value = random.randint(1, 100)
    data.append(value)

#print the list
print("Here is a random list:")
for i in range(20):
    print(data[i], end=" ")

    # check how many of the numbers are even
    if int(data[i]) % 2 ==0:
        j = j+1

print()
print("Out of those 20 numbers:", j ,"of them are even" )
