encrypted_text = input("Enter the text that you want to decrypt:")
Key = input("Enter the key:")

G = [int(e) for e in encrypted_text.split(",")]
decrypted_text = ""
for i in range(len(G)):
    decrypted_text += chr(G[i] ^ ord(Key[i % len(Key)]))

file = open("Decrypted.txt", "w")
file.write(decrypted_text)
file.close()
