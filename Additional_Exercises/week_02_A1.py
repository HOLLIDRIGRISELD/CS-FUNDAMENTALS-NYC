number = int(input("give me a number for the length of the pattern: "))

for i in range(number):
    if i % 2 == 0:
        print("% ", end='') 
    else:
        print("# ", end='')


print("  Made by Seldi Hollidri")