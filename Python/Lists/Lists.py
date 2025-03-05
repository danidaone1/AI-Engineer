list=["a","b","c","d","e"]
print(list)
print(list[1])
list[1]="x"
print(list)
print(list[0:3])
list.append("z")
print(list)
list.insert(0,"W")
print(list)

list=["a","b","c","d","e"]
list2=[1,2,3,4,5]
test=list+list2
print(test)
print(len(test))
print(1 in test)
print(12 in test)
print("a" in test)