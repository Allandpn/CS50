class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.size = 0


    def __str__(self):

        return f"{'🍪'*self.size}"



    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self._size += n


    def withdraw(self, n):
        if self.size - n < 0:
            print(ValueError)
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, n):
        self._capacity = n

    @size.setter
    def size(self, n):
        self._size = n


def main():
    jar = Jar()

    print(str(jar.capacity))

    print(str(jar))

    jar.deposit(12)

    print(str(jar))

    jar.withdraw(1)

    print(str(jar))



main()