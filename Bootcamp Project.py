import hashlib
import random

user_input = input("Enter your password: ")
str_ = ""
for i in range(1, len(user_input)+1):
    num = random.randint(1, 100)
    if i % 3 == 0:
        if num % 2 == 0:
            str_ = user_input[:i] + str(num) + user_input[i:]
print(str_)
message = str_.encode()
print("MD5:", hashlib.md5(message).hexdigest())
