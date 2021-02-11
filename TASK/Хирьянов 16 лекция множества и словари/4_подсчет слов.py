import timeit

code_to_test = """
import string

text = open('datafile.txt')
lines = text.readlines()

T = ''
for line in lines:
    T +=line.rstrip()
for i in string.punctuation:
    T = T.replace(i, ' ')
T = T.lower()

keys = []
for i in T.split():
    if i not in keys and len(i) > 3:
        keys.append(i)
keys.sort(key=len)

value = []
for i in keys:
    x = T.count(i)
    value.append(x)

Count = {k:v for (k,v) in zip(keys,value)}

max_value = max(Count.values())
word = {k: v for k, v in Count.items() if v == max_value}
print(word)
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


