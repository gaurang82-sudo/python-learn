def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz" if input % 5 != 0 else "fizz_buzz"

    elif input % 5 == 0:
        return "Buzz" if input % 3 != 0 else "fizz_buzz"
    else:
        return input


print(fizz_buzz(15))
