import base64

text = "Hello$World"

encoded = base64.b64encode(text.encode())

print("Base64: ",encoded.decode())