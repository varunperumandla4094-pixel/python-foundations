# Day 3 - List Traversal

# Exercise 1: Print every element
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# Exercise 2: Count list elements
count = 0

for num in numbers:
    count += 1

print("Total elements:", count)


# Exercise 3: Sum of even numbers
numbers = [3, 7, 2, 9, 4]

total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of even numbers:", total)
