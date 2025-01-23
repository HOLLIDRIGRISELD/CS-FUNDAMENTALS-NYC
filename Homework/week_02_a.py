#The operator % gives the remainder of the division between 2 numbers.
#For example: 10 % 2 = 0, 10 % 3 = 1, 10 % 4 = 2. 
# Write a program to ask a user for a year and find if the year is a leap year or not. 
#Leap years are divisible by 4.
#Exception: if a year is divisible by 4, and by 100 is not a leap year, unless if it is divisible by 400, too.

#input stage
year = int(input('Give me a year please : '))

#caclulation stage to find leap year

if (year % 4 != 0):
    print("the year :",year,"is NOT a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("the year :",year,"IS a leap year")
elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 !=0):
    print("the year :",year,"is NOT a leap year")
elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 ==0):
    print("the year :",year,"IS a leap year")