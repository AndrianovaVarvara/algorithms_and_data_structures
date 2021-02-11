import string

file = open("en-ru.txt", encoding="utf-8")
on_string = file.read().split("\n")
dict = dict()

for item in on_string:
    key = item.split("\t-\t")[0]
    value = item.split("\t-\t")[1:]
    dict[key] = value
file.close()


t = open("input.txt", encoding="utf-8")
text = t.read().lower().split()
myString = ' '.join(text)  # превращаем в строку
for i in string.punctuation:
    myString = myString.replace(i, ' ')
text = myString.split() # после замены знаков обратно в список
t.close()


Perevod = open('output.txt', 'w')
for i in text:
    if dict.get(i) == None:
        Perevod.write(i)
    else:
        Perevod.write(str(dict[i]))
Perevod.close()



