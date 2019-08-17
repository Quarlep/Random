text = input("Enter the message that you want to encrypt:")
key = input("Enter the key:")

g = ""
for i in range(len(text)):
    g += text[i]

encrypted_text = ""
for i in range(len(g)):
    encrypted_text += str(ord(g[i]) ^ ord(key[i % len(key)])) + ","


encrypted_text = encrypted_text[:-1]

file = open("Encrypted.txt", "w")
file.write(encrypted_text)
file.close()
