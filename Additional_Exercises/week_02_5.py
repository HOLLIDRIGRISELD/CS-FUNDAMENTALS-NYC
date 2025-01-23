number = int(input("give me a number: "))

for i in range(number):
    for j in range(i + 1):  #with i + 1 the need amount of stars will be typed
        print('*', end=' ') #copied from the hints
    print() 

print("made by Seldi Hollidri")