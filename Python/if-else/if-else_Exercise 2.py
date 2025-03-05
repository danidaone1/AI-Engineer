#Question: 2 Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100. 
#Question: I .Ask user to enter his fasting sugar level
#Question: II .If it is below 80 to 100 range then print that sugar is low
#Question: III .If it is above 100 then print that it is high otherwise print that it is normal

user_sugar=input("Please enter your sugar level: ")
user_sugar=float(user_sugar)
if user_sugar >100:
   print("Sugar is high")
elif user_sugar <80:
   print("Sugar is low")
else:
   print("Sugar is normal")
