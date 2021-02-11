import hashlib

# print(hashlib.algorithms_available) #  список всех алгоритмов, доступных в системе
# print(hashlib.algorithms_guaranteed) # алгоритмы модуля

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

