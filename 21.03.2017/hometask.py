#3

class Figure:

    def __init__(self,first_side,second_side):
        self.first_side = first_side
        self.second_side = second_side

    def fprint(self):
        msg = "Triangles and Rectangles"
        return msg


class Rectangle(Figure):

    def msg(self):
        print("This is rectangle")

    def _square_a(self):
        s = self.first_side * self.second_side
        return s

    def __perimeter(self):
        p= self.first_side * self.second_side * 2
        return p


class Triangle(Figure):

        def msg(self):
            print("This is triangle")

        def _square_a(self):
            self._side = self.second_side / 2
            s = self.first_side * self._side
            return s

        def __perimeter(self):
            self.__side = pow(self.first_side**2 + self.second_side**2, 0.5)
            p = self.first_side + self.second_side + self.__side
            return p

some_triangle = Triangle(5,10)
print(some_triangle._square_a())
print(some_triangle._side)
#print(some_triangle.__perimetr)
#print(some_triangle.__side)
#print(some_triangle._Figure__perimeter)
print(some_triangle._Triangle__perimeter())


#6
class Iterator(object):

    def __init__(self,file_name):
        self.data = open(file_name)

    def __iter__(self):
        return self

    def __next__(self):
        items = self.data.readline()
        if items:
            items = items.rstrip("\n")
            return items
        raise StopIteration

file_to_iter = Iterator("file.txt")
while file_to_iter.__iter__:
    print(file_to_iter.__next__())


class Iterator_l(object):

    def __init__(self,my_list):
        self.data = my_list
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.el = self.data[self.count]
        if self.el in self.data:
            self.count += 1
            return self.el
        else:
            raise IndexError



my_list = [99, 999, 9999, 9]
list_to_iter = Iterator_l(my_list)
for i in list_to_iter:
    print(list_to_iter.el)



class Iterator_d(object):

    def __init__(self,my_dict):
        self.data = my_dict
        self.count =0

    def __iter__(self):
        return self

    def __next__(self):
        self.el = list(self.data.values())
        self.i = self.el[self.count]
        if self.i in self.el:
            self.count += 1
            return self.i
        else:
            raise IndexError



my_dict = {"first":"one", "second":"two", "third":"three"}
dict_to_iter = Iterator_d(my_dict)
for j in dict_to_iter:
    print(dict_to_iter.i)



#7
def generator():
    for x in range(100):
        if x % 3 == 0:
            yield x
    else:
        pass
for i in generator():
    print(i)


#8
l_compr = [x for x in range(100) if x % 3 == 0]
print(l_compr)

