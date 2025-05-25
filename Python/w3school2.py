i=0
while i<10:
    i+=1
    if i==6:
     continue
    print(i)
    if i==9:
       break
else:
   print("Loop is now complete")

rows=5       
for x in range(1,rows+1):
   for y in range(0,6):
     print("*",end="")#Stay on the same line
   print()

#Right hand triangle
for q in range(1, rows+1):
   for w in range(q):
      print(" *",end="")
   print()   
#Inverted triangle
for a in range(rows,0,-1):
   for b in range(a):
      print(" *",end="")
   print() 

#left hand triangle
for f in range(1,rows+1):
   for g in range(rows-f):
      print(" ",end="")
   for h in range(f):
      print("*",end="")
   print()      
#Pyramid
for y in range(1,rows+1):
   for u in range(rows-y):
      print(" ",end="")
   for t in range(y):
      print(" 1",end="")
   print()
for b in range(1,rows+1):
   for n in range(b):
      print(" ",end="")
   for m in range(rows-b):
      print(" 1",end="")
   print()      

      
