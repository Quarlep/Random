from random import choice
from string import ascii_letters, digits

list_of_str = ascii_letters + digits + "?!"

password = ""
for i in range(15):
    pass_dig = choice(list_of_str)
    password += pass_dig

print(password)

