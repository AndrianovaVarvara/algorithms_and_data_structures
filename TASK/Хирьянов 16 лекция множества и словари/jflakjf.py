import timeit

code_to_test = """
import re
import string
frequency = {}
document_text = open('datafile.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)