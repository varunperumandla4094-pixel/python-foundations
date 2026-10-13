numbers = [10, 25, 5, 25, 8, 25, 15]

largest = numbers[0]
count = 0

for num in numbers:
    if num > largest:
        largest = num
        count = 1

    elif num == largest:
        count += 1

print("Largest number:", largest)
print("Occurrences:", count)
