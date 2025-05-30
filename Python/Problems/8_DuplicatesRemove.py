#8. Remove Duplicates from a List
#Remove duplicate elements and return a new list.
mylist=[1,2,3,4,5,3,4,5]
newlist=[]
print("Old list",mylist)
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(newlist)
    
     