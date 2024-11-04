a = int(input("give me a starting point number : "))
b = int(input('give me an ending point number : '))
c = int(input("give me a nuber to use as a step :"))
print()

if a < b:
    for i in range(a,b+1,c):
        print(i, end=' ')
elif a > b:
    for i in range(a,b+1,-c):
        print(i , end=" ")

print()
print("made by Seldi Hollidri")