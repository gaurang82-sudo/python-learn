def greet(first_name, last_name):
    print(f"hello {first_name}  {last_name}")
    # print("welcome aboard")


greet("gaurang", "patel")


def get_greeting(name):
    return f"Hi {name}"


print(get_greeting("gaurang"))


def increment(number, by):
    return number + by


print(increment(2, 5))


def increment_by(number, by=1):
    return number + by


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 8, 4, 6, 9))


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="gaurang", age=20)
