temprature = 35
if temprature > 30:
    print("It's warm")
    print("Drink water")
elif temprature > 20:
    print("It's nice")
else:
    print("It's cool")
print("Done")


age = 12

massage = "eligible" if age >= 18 else "not eligible"
print(massage)


high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")

age = 22
if 18 <= age < 65:
    print("eligible")


for number in range(1, 10, 2):
    print("Attempt", number, number*".")


successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")


for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

command = ""
while command.lower() != "quit":
    command = input(">")
    print(command)
