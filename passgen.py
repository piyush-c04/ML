import string
import random
s1 = list(string.ascii_uppercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
passlength = int(input("Enter the password length"))
s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s) 
"""
random.sample(s,plen*2)

"""
print("password is: ")
print("".join(s[0:passlength]))
