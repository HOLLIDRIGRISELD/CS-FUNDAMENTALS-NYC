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

print("made by Seldi Hollidri")