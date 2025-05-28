#Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#[g,o,o,g,l,e,.,c,o,m]

string="google.com"
count={}
char=''
for char in string:
    if char in count:
        count[char] +=1
    else:
        count[char]=1


print(count)
