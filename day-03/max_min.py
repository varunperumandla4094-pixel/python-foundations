numbers = [25, 7, 89, 12, 3, 65, 42]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)