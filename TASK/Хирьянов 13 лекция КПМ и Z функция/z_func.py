def z_func(s):
    n=len(s)
    l, r = 0, 0
    z = [0] * len(s)
    for i in range(1, n-1):
        if i<=r:
            z[i] = min(z[i - l], r - i+1)
        while i+z[i] < n and s[z[i]] == s[i + z[i]]:
          z[i] += 1
        if i + z[i]-1 > r:
          l, r = i, i + z[i]-1
    return z

print(z_func('abacabacaba'))