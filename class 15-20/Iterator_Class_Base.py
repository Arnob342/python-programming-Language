class IteratorClasss:
    def __init__(self):
        print("Constructor")

    def __iter__(self):
        self.num = 3
        # return self.num # TypeError: iter() returned non-iterator of type 'int'
        return self

    def __next__(self):
        getNum = self.num
        self.num *= 3
        return getNum

    def __del__(self):
        print("Destructor")


itr = IteratorClasss()
my_item = iter(itr)

print(next(my_item))
print(next(my_item))
print(next(my_item))
print(next(my_item))
print(next(my_item))
print(next(my_item))
print(next(my_item))
print(next(my_item))
print(next(my_item))
