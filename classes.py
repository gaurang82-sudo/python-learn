from abc import ABC, abstractmethod


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"poin ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, values):
        if values < 0:
            raise ValueError("prices cannont be negative")
        self.__price = values


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.wight = 12
        super().__init__()

    def walk(self):
        print("walk")


class Fices(Animal):
    def swing(self):
        print("swing")


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            print("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            print("Stream is alredy cloased")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data froam a file ")


class NetworkStream(Stream):
    def read(self):
        print("Reading data froam a network stream ")


class Text(str):
    def duplicate(self):
        return self + self


point = Point(1, 2)
other = Point(1, 2)
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
print(point.x)
point.draw()
another = Point(2, 9)
another.draw()
print(another.default_color)
print(Point.default_color)

Point.default_color = "yellow"
print(another.default_color)
print(Point.default_color)
print(point)


zeros = Point.zero()
zeros.draw()
print(point == other)
combine = point + other
print(combine.x)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")

print(cloud["python"])
print(len(cloud))
cloud["python"] = 9
print(cloud["python"])
print(cloud.__dict__)
print(cloud._TagCloud__tags)

prod = Product(10)
print(prod.price)


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Animal))
print(m.wight)
