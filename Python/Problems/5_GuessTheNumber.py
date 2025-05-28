import random
rand_num=int(random.randint(1,10))
print(rand_num)
print("Enter your number")
guess=0
while rand_num!=guess:
    print(rand_num)
    guess=int(input())
    print("Wrong Try Again")
else:
    print("You guessed right")