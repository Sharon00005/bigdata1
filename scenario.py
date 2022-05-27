class numbers:

  def __iter__(self):

    self.n = 1

    return self

  def __next__(self):

    x = self.n

    self.n += 1

    return x



myclass = numbers()

myiter = iter(myclass)



print(next(myiter))

print(next(myiter))

print(next(myiter))
