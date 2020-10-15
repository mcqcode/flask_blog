from hashlib import sha256

x = sha256('123'.encode('utf-8')).hexdigest()
print(x)