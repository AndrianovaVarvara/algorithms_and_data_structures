def prefix_func(s):
    # pi = [[0]* len(s)]
    # j=0
    # i=1
    # while j<=len(n):
    #     if s[i]==s[j]:
    #         pi[i]=j+1
    #         i+=1
    #         j+=1
    #     else::
    #         if j==0:
    #             pi[i] = 0
    #             i+=1
    #         else:
    #             j=pi[j-1]
    pi = [[0] * len(s)]
    for i in range(1, len(s)):
        p = pi[i-1]
        while p > 0 and s[i] != s[p]:
            p = pi[p-1]
        if s[i] == s[p]:
            p += 1
        pi[i] = p
    return pi

def kmpSearchByCompil(s, n):
    pi = [[0] * len(s)]
    temp = n + '#' + s
    for i in range(1,len(temp)):
        j = pi[i-1]
        while j > 0 and temp[j] != temp[i]:
            j = pi[j-1]
        if temp[j] == temp[i]:
            j += 1
        pi[i] = j
        if j == len(n):
            return i
    return None

kmpSearchByCompil('abdabeabfabc', 'abc')