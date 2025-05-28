#6. Count Vowels and Consonants
#From a sentence, count vowels and consonants separately.

sentence="the quick brown fox jumps over the lazy dog"
cons_count=0
vowels_count=0
vowels=["a","e","i","o","u"]
for i in sentence:
    if i in vowels:
        vowels_count +=1
    elif i==" ":
        continue
    else:
        cons_count+=1
print(vowels_count)
print(cons_count)
