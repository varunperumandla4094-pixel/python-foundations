n = int(input("Enter a number:"))
count = 1
total = 0

while count <= n:
    total = total + count
    count += 1

print("Final total:", total)