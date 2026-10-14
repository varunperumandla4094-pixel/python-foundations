# 1. Sum of even numbers
def sum_even_numbers(numbers):
    total = 0

    for num in numbers:
        if num % 2 == 0:
            total += num

    return total


print("Even sum:", sum_even_numbers([3, 6, 9, 12, 5, 8]))
print("Even sum:", sum_even_numbers([1, 3, 5, 7]))


# 2. Find the largest number
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


print("Largest number:", find_largest([12, 45, 7, 89, 23]))
print("Largest number:", find_largest([-8, -2, -15]))
print("Largest number:", find_largest([42]))
