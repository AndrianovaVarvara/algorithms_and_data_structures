file = open("english-russian.txt", encoding="utf-8")
on_string = file.read().split("\n")
dict = dict()
for item in on_string:
    key = item.split("\t-\t")[0]
    value = item.split("\t-\t")[1:]
    dict[key] = value
file.close()
dict_reversed = {}
for i in dict:
    for j in dict[i]:
        if j not in dict_reversed:
            dict_reversed[j] = set([i])
        else:
            dict_reversed[j].add(i)

ks = list(dict_reversed.keys())
ks.sort()
for k in ks:
    print(k,dict_reversed[k])
