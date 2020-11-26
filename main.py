# Python 很多類別已經用了 Iterator pattern, 例如 collection, sequence (such as: string, list, tuple), non-sequence (such as: dict, file object, objects of any class with __iter__() or __getitem__() impletmented)
mytuple = ("apple", "banana", "cherry")
another_tuple = "apple", 
print(type(another_tuple))

for i in mytuple:
    print(i)

# 利用 iterator 可以省記憶體, 同時使用的空間
myit = iter(mytuple)

print(next(myit))





# 定義你自己的 iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        print(type(self))
        return self

    def __next__(self) -> int:
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# list
# define a list
print('--- list 也是 iterator ---')
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))
print('---------- list them all ---')

# iterable
# create an iterator object from that iterable
iter_obj = iter(my_iter)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

print('---------- xxxx ---')
# class example
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(5)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#print(next(i)) # cause exception

# yeild in generator
input('press ENTER to start infinity number generator:')
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")
