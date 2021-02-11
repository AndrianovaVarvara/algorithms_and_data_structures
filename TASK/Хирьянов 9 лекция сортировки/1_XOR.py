a = int(input("First hex: "), 16)
b = int(input("Second hex: "), 16)

print("{0:x} xor {1:x} = {2:x}".format(a, b, (a ^ b)))
