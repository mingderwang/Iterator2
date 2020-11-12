# Python 很多物件已經用了 Iterator pattern
mytuple = ("apple", "banana", "cherry")

for i in mytuple:
  print(i)

# 利用 iterator 可以省記憶體, 同時使用的空間
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# 定義你自己的 iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
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