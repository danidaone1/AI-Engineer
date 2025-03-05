india=["mumbai",
       "banglore",
       "delhi"]

pakistan=["lahore",
          "karachi",
          "Islamabad"]

bangladesh=["dhaka",
            "khulna",
            "rangpur"]
#Question: i Write a program that asks user to enter a city name and it should tell which country the city belongs to
#cName=input("Enter a city name: ")
if cName in india:
    print("The city name is in the country India")
elif cName in pakistan:
    print("The city name is in the country Pakistan")
elif cName in bangladesh:
    print("The city name is in the country Bangladesh")
#Question: ii Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
#cityOne=input("Enter they name of first city: ")
#cityTwo=input("Enter they name of Second city: ")
if cityOne and cityTwo in india:
 print("Both cities are in India")
elif cityOne and cityTwo in pakistan:
   print("Both cities are in pakistan")
elif cityOne and cityTwo in bangladesh:
   print("Both cities are in bangladesh")
else:
   print("They are not in the same country")

#Question: 2 Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100. 
#Question: I .Ask user to enter his fasting sugar level
#Question: II .If it is below 80 to 100 range then print that sugar is low
#Question: III .If it is above 100 then print that it is high otherwise print that it is normal

user_sugar=input("Please enter your sugar level: ")
if user_sugar >=80 and 100:
   print("Sugar is high")
elif user_sugar <= 80 and 100:
   print("Sugar is low")
elif user_sugar in 80 and 100:
   print("Sugar is normal")


     