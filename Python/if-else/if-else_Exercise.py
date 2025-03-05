india=["Mumbai",
       "banglore",
       "delhi"]

pakistan=["lahore",
          "karachi",
          "Islamabad"]

bangladesh=["dhaka",
            "khulna",
            "rangpur"]
#Question: 1 Write a program that asks user to enter a city name and it should tell which country the city belongs to
cName=input("Enter a city name: ")
if cName in india:
    print("The city name is in the country India")
elif cName in pakistan:
    print("The city name is in the country Pakistan")
elif cName in bangladesh:
    print("The city name is in the country Bangladesh")
