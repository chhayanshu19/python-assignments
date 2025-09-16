import hashlib

stored = hashlib.sha256("12345".encode()).hexdigest()

u = input("Enter username: ")
p = input("Enter password: ")

hashed = hashlib.sha256(p.encode()).hexdigest()

if hashed == stored:
    print("Login Successful")
else:
    print("Invalid credentials")

# Hashing is one-way (cannot be reversed). We hash both stored and input, then compare.