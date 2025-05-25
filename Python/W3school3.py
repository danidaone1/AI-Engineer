mytuple=("Dani",295,30,40,"Faraz bharwa")
print(len(mytuple))

for x in mytuple:
    print(f"My tuple values: {x} ")

print(mytuple[0:-1])

print(mytuple[3])

#Changing tuple value using list
mylist=list(mytuple)
mylist[1]="Mohamid"
mytuple=tuple(mylist)
print(mytuple)

tuple2=("banana",)
mytuple=mytuple+tuple2
print(mytuple)

del tuple2
#tuple unpacking
(name1,name2,*list1)=mytuple
print(name1)
print(name2)
print(list1)

i=0
while i<len(mytuple):
 print(mytuple[i])
 i+=1

metuple=mytuple*2
print(metuple)

print(mytuple.index("Mohamid"))

#Set
myset={1,2,3,4,5,"apple","banana"}
print(myset)

for x in myset:
   print(x)

#Duplicates are ignored in a set
set2={3,4,5,6,7,8}
myset.update(set2)
print(myset)

set1={1,2,3,4,5}
set3={6,7,8,9,0}
set4={1,2,3,6,7}
set5={4,5,8,9,0}
reset=set1.union(set3,set4,set5)
print(reset)

reset1=set1.intersection(set4)
print(reset1)
#difference() method keeps the item in first set that are not in the other set
#symmetric_difference() method returns all the values except duplicates
rest1=set1.symmetric_difference(set4)
print(rest1)
#dictionary

dick=dict(name="Daniyal",age=22,height="6'3")
print(dick)

print(dick.get("name"))
y=dick.keys()
print(y)
dick["color"]="Brownish"
print(y)

y=dick.values()
print(y)
print(dick)
for x in dick:
   print(x)
y=dick.items()
print(y)
dick["weight"]=110
print(y)

#update a dictionary
dick.update({"weight":115})
print(dick)

dick.pop("weight")
print(dick)

#looping through dictionaries
for x,y in dick.items():
   print(x,y)

for x in dick.values():
   print(x)

uw=list(dick.items())
print(uw)

temp=[]
temp2=[]
for x in range(len(uw)):
     print(x)
     temp.append(list(uw[x]))
     for y in range(len(temp[x])):
        temp2.append(temp[x][y])
print(temp)
print(temp2)
we=dick.copy()
print(we)

#nest dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x,obj in myfamily.items():
   print(x)
   for z in obj:
      print(z+":",obj[z])
      