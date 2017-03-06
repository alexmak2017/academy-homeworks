from random import randint
import part_2
d = {"first_name": "Alexandr",
    "Last_name": "Filipov",
    "email": "alex@ukr.net",
    "age": 27
    }

b = []
for i in d.values():
    if type(i) == str and len(i) > 5 and "a" in i:
        b.append(i)
    if type(i) == int and 25 <= i < 40:
        b.append(i)
print(b)

c = []
for j in b:
    if "n" not in str(j) and "m" not in str(j):
        c.append(j)
print(c)
"""
for k in b:
    if "n" in str(k) or "m" in str(k):
        b.remove(k)
print(b)
"""

n = ["ax","bx","cx"]
n.reverse()
print(n)

f = []
for i in b:
    if type(i) == int:
        i = str(i)
    f.append(i)
d = ','.join(f)
print(d)
m = d.split(",")
print(m)



for i in range(randint(20,40)):
    print(part_2.type_check(i))