""" Random Password Generator """

import random 
import string

pass_len = 12

charVal = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charVal)

print("Your password is: ",password)