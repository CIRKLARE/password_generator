#!/bin/python

import string, secrets

x = int(input("length of password > "))

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(x))

print(password)