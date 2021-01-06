course = "python programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# coment
course = "Python \"Programming"
print(course)
# \'
# \"


first = "Mosh"
last = "Hamedani"
full = f"{first} {last}"  # or full = first + " " + last
print(full)

course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swif" not in course)


print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)


x = 10
x += 3  # or x = x +3

x = input("x :")
y = int(x) + 1
print(f"x:{x}, y:{y}")
# int()
# str()
# bool()
# float
