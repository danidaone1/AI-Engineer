#4. Login System
#Store users in a dict and allow login (3 attempts).

users={
    "dani":"1234",
    "faraz":"abcd",
    "mohamid":"xyz"
}
total_tries=3
tries_count=0
run=True
fail_check=True
print("Please Type input 1,2,3 for the available options")
print("1.Login")
print("2.Register")
print("3.Exit")
user_select=int(input())
match user_select:
    case 1:
     print("First option selected")
     username=input("Please enter your Username")
     password=input("Please enter your password")
     for key,value in users.items():
        if key in username and value in password:
            print("Login Succesfull")
            break
        else:
            fail_check=False
            continue
     if fail_check==False:
         print("Login Failed")

            
        
    case 3:
          run=False

                
           
           

 