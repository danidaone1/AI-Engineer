7#. Fibonacci Generator
#Print first `n` Fibonacci numbers.
sequence=[0,1]
for i in range(20):
    sequence.append(sequence[i]+sequence[i+1])
print(sequence)