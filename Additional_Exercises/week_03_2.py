data = [56, 12, 45, 11, 37, 73, 57, 33, 15, 81]

print("Here is a list:")
for i in range(len(data)):
    print(data[i], end=" ")

print()
print("The list backwards will be:")
for i in range(len(data) - 1, -1, -1):
    print(data[i], end=" ")

