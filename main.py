import random

chars = input('Write symbols:'+"\n")

number = input('Password count:'+"\n")
length = input('Password length:'+"\n")

number = int(number)
length = int(length)

for n in range(number):
    password = (''+'\n')
    for i in range(length):
        password += random.choice(chars)
    print(password)
