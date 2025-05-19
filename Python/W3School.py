a=" Faraz"
print(a.upper())

print(a.lower())
#This removes the whitespace
print(a.strip())

x=a[0:4]

print(x.replace("a","A",1)) 
x=x.replace("a","A",1)
x=x+a[4:]
print(x)


b="Daniyal , Hassan"
print(b.split(","))

age=22
name= "daniyal hassan"
s=f"My name is "+name+f" and my age is {age:5f}"
print(s)

w=f"Faraz mere paise de {10*100}"
print(w)

i="Faraz is bharwa and a \" bitch\" hehe!"
print(i)

print(type(age))

print(isinstance(age,float))
#Identity opreator 
a=10
b=100
print(a is b)

print(a is not b)

#Memebership Opreators
str1="Daniyal Hassan"
print("Daniyal" in str1)

print("Daniyal" not in str1)