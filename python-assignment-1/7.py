from cryptography.fernet import Fernet 

# generate key

key = Fernet.generate_key()
cipher = Fernet(key)

# original password
username = "Chhayanshu"
passwrd = "12345"
encrypted = cipher.encrypt(passwrd.encode())

# Input password
u = input("Enter username: ")
p = input("Enter password: ")

if cipher.decrypt(encrypted).decode() == p:
    print("Login Successful")
else:
    print("Invalid credentials")

# We encrypt the stored password and decrypt for comparison.
