colors = ["Red","Green","White","Blue","Violet"]

ask =input("Tell me a color you want your car:")
flag = False
for i in range(len(colors)):
    if colors[i] == ask:
        flag=True
    


if flag:
    print("Nice!...There is a car with the color you asked!")
else:
    print("Im sorry your we cant find a car this color")

