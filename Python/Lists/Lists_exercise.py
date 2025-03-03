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
