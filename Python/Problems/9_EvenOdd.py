#9. Number Categorizer
#Given a list of numbers, print "Even", "Odd", or "Zero" for each.

mylist=[1,2,4,5,6,0,8,9,0,4,2,6,5,7]
for i in mylist:
    if i%2==0:
        print(f"Even: {i}")

    elif i%2!=0:
        print(f"Odd: {i}")
    if i==0:
        print(f"Zero: {i}")




