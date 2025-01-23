#Ask user for 3 numbers, a, b, and c. 
# First number is the starting point, second number is the end point, and third number is the step.
#Then, print values from a to b, with a c step. 
# If a is greater than b, then step down from a to b. 

#input for a b and c 
a = int(input("Give me a starting point number  : "))
b = int(input('Give me an ending point number   : '))
c = int(input("Give me a nuber to use as a step :"))
print()

#check in what direction the loop will go
if a < b:
    for i in range(a,b+1,c):
        print(i, end=' ')
elif a > b:
    for i in range(a,b+1,-c):
        print(i , end=" ")