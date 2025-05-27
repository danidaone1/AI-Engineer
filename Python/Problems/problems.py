#Question: 1 Find max in a list
def find_max(milist):
        maxx=milist[0]    
        for i in milist:
             if i>maxx:  
              maxx=i
        return maxx              
mylist=[11,2,3,4,5,6,7,9,10,15]
print(max(mylist))

#Question: 2 check if a list reads the same forward and backward  Palindrome checker
palin=["a","b","b","a"]
length=len(palin)//2
list2=palin[:length]
list3=palin[length:]
print(list2)
print(list3)
