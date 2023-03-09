"""
1. WAP to generate a random color hex, a random alphanumerical string, random value,
random value between two integers, random multiple of 7 between 0 and 70
hint: use random.randint()
"""
import random
import string
r= random.randint(0,255)
print('#%02X%02X%02X' % (r(),r(),r()))

res = ''.join(random.choices(string.ascii_letters +
                             string.digits, k=7))
print(res)


print(random.randint(0,9))

