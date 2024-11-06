import random

data = []
j = 0
for i in range(20):
    value = random.randint(1, 100)
    data.append(value)

print("here is a random list:")

for i in range(20):
    print(data[i], end=" ")
    if int(data[i]) % 2 ==0:
        j = j+1

print()
print("out of those 20 numbers: ", j ,"of them are even" )
