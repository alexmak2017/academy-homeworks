print("Hello world")
a=2017.74
b="Hello"
c="World"
print("{1} {2} - {0}!".format(int(a), b, c))
my_list=[25,True,"string",[1,2,3],{"first":1,"second":2}]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
try:
    print(my_list[7])
except IndexError:
    print("There is no such index")
print(str("123.456"))
print(str(float(93735)))
