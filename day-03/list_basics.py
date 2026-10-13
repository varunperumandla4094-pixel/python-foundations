numbers = [10, 20, 30, 40, 50]

numbers[2] = 100

print("First number:", numbers[0])
print("Last number:", numbers[-1])
print("Updated list:", numbers)


shopping = ["rice", "milk", "eggs", "milk"]

shopping.append("bread")
shopping.remove("milk")
removed = shopping.pop()

print("Shopping list:", shopping)
print("Removed item:", removed)
