#Question: 2 check if a list reads the same forward and backward  Palindrome checker
palin=["a","b","c","b","c","b","a"]
length=len(palin)//2
first=palin[:length]
second=palin[length:]
palin_flag=True
print(first)
print(second)
for i in range(length):
     if first[i]==second[(i+1)*-1]:
         palin_flag=True
     elif first[i]!=second[(i+1)*-1]:
          palin_flag=False
          break
if palin_flag==True:
     print("The given string is Palindrome")
else:
     print("The given string is not palindrome")
