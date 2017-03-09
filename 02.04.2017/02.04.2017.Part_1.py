from random import randint
import part_2
<<<<<<< HEAD
d = {"first_name": "AlexaNdr",
    "Last_name": "Filipov",
    "email": "alex@ukr.Net",
    "age": 27
=======
d = {
        "first_name": "Alexandr",
        "Last_name": "Filipov",
        "email": "alex@ukr.net",
        "age": 27
>>>>>>> 8bfb3266a9ef885a8c6cf3313fd1eb24b0515bb2
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
    if type(j) != str:
        j = str(j)
    if "n" not in str(j.lower()) and "m" not in str(j.lower()):
<<<<<<< HEAD
        c.append(j)
=======
>>>>>>> 8bfb3266a9ef885a8c6cf3313fd1eb24b0515bb2
print(c)

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
