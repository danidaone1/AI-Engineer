for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print("")

for x in range(4):
    for a in range(x+1):
        print(" ",end="")
    for y in range(4-x):
        print("* ",end="")
    print("")
        