from timeit import timeit
try:
    age = int(input("Age:"))
except ValueError as ex:
    print("you didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("no excptions ")
print("hello")


try:
    file = open("ex1.py")
    age = int(input("Age :"))
    x = 10/age
except ValueError:
    print("you didn't enter a valid age")
except ZeroDivisionError:
    print("you didn't enter a valid age")
finally:
    file.close()

# with

try:
    with open("ex1.py") as file:
        print("file opende")

    age = int(input("Age :"))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")

code1 = """
def calulate_Xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less")
    return 10 / age


try:
    calulate_Xfactor(-2)
except ValueError as ex:
    pass
"""

code2 = """
def calulate_Xfactor(age):
    if age <= 0:
        None
    return 10 / age


x = calulate_Xfactor(-2)
if x == None:
    pass

"""
print("coede1 = ", timeit(code1, number=10000))

print("coede2 = ", timeit(code2, number=10000))
