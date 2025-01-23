import random

data = []

for i in range(100):
    value = random.randint(1, 50)
    data.append(value)


print("here is a random list:")

for i in range(len(data)):
    print(data[i], end=",")
print()

number = int(input("give me a number and i will tell you how many time it is typed in the list above : "))
count= 0
for i in range(len(data)):
    if number == data[i]:
        count = count +1

print("the numver you given me is in the list : ",count, " times!")