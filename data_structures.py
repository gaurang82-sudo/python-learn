from collections import deque
from array import array
# list
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(letters[0])
print(letters[1:2])

letters[0] = "A"
print(letters)
number = [1, 2, 3, 4, 5]

first, second, *other = number

letters.append("d")
letters.insert(0, "g")
letters.pop(2)
letters.remove("c")

print(letters)
print(letters.index("A"))

numbers = [3, 15, 4, 48, 75, 11]
numbers.sort()
print(numbers)
numbers = [3, 15, 4, 48, 75, 11]
numbers.sort(reverse=True)
print(numbers)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


def short_item(item):
    return item[1]


items.sort(key=short_item)
print(items)
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


print(items)
items.sort(key=lambda item: item[1])
print(items)


prices = list(map(lambda item: item[1], items))
print(prices)
#prices = [item[1] for item in items]
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
filtered = [item for item in items if item[1] >= 10]  # list_comprehensions
print(filtered)

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
print(list(zip("hiiii", list1, list2)))
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
# stack
print(browsing_session)
browsing_session.pop()
print(browsing_session)

# queue

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)


# tupal


point = (1, 2) + (3, 4)
point1 = (1, 2) * 3

print(point, point1)
print(point[1])


x = 10
y = 11
x, y = y, x
print("x", x)
print("y", y)


num = array("i", [1, 2, 3])
print(num[1])


number = [1, 2, 1, 3, 4]
first = set(number)
second = {1, 5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)


# dictonaries

point = {"X": 1, "y": 2}

print(point["X"])


values = {x: x * 2 for x in range(5)}
print(values)


# generator

values = (x * 2 for x in range(10))
print(values)
