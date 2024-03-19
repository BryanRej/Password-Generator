import string
import random

def generate_password(length = 16):
  characters = string.printable
  password = "".join(random.choice(characters) for i in range(length))
  return password

password = generate_password()
print("Your random password is:" + password)