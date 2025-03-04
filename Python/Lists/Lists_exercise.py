exp=[2200,2350,2600,2130,2190]
#Question: 1 In Feb, how many dollars you spent extra compare to January?
print("Dollar spent in Feb compared to january: ",exp[1]-exp[0])

#Question: 2 Find out your total expense in first quarter (first three months) of the year.
print("Total expense in first quarter: ",exp[0]+exp[1]+exp[2])

#Question: 3 Find out if you spent exactly 2000 dollars in any month
print("Exactly spent 2000 in any month: ",2000 in exp)

#Question: 4 June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Total expense list after june: ",exp)

#Question: 5 You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3]=exp[3]-200
print("Updated expense List of april",exp)

#Question 2.0
heros=['spider man','thor','hulk','iron man','captain america']
#Question: 1 Length of the list
print(len(heros))

#Question: 2 Add 'black panther' at the end of this list
heros.insert(5,'black panther')
print(heros)

#Question: 3 You realize that you need to add 'black panther' after 'hulk',
#so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
print(heros)

heros.insert(3,'black panther')
print(heros)

#Question: Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#  Do that with one line of code.
heros[1:3]=['Doctor strange']
print(heros)
#Question: 5 Sort the list in alphabetical order
heros.sort()
print(heros)
