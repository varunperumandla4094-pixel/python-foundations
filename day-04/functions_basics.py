# 1. Defining and calling a function
def say_welcome():
    print("Welcome to Day 4!")


say_welcome()
say_welcome()


# 2. Functions with parameters
def calculate_area(length, width):
    area = length * width
    print("Area:", area)


calculate_area(5, 4)
calculate_area(10, 3)


# 3. Functions with return values
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(50, 3)
print("Total cost:", total)


# 4. Functions with conditions
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"

    return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))
print(check_even_odd(0))
