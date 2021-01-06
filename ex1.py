even_number_count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        even_number_count += 1

print(f"we have {even_number_count} even between 1 to 10")
