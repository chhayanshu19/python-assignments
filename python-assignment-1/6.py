username = "Chhayanshu"
password = "12345"

print("-----Sign In-----")
u = input("Enter Username: ")
p = input("Enter Password: ")

if(u == username and p == password):
    print("Welcome",username)
else:
    print("Invalid Crediantials!")