def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("Bella")

def area_of_circle(radius):
    pi = 3.14
    area_of_circle = pi * radius**2
    return print(area_of_circle)
area_of_circle(4)

def min_max_temps(readings):
    return print(min(readings), max(readings))

readings = [15, 14, 17, 20, 23, 28, 20]
result = min_max_temps(readings)
print(result)


def is_weekend(day):
    if day == 6 or day == 7:
        return print("It's the weekend!")
    else:
        return print("It's not the weekend")
is_weekend(7)
    
def fuel_efficiency(distance, fuel_used):
    return print(distance/fuel_used)
fuel_efficiency(300, 10)

def secret_code(n):
    last_digit = n % 10
    rest = n // 10
    digits = len(str(rest))
    return last_digit * (10 ** digits) + rest
secret_code(12345)

def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result
print(power(2, 3))

def find_min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return(smallest, largest)

readings = [2, 10, 14, 8, 23, 17, 19]
print(find_min_max(readings))

numbers = [10, 4, 23 , 7, 15]

min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num 

print(f"Minimum value: {min_value}")

max_value = numbers[0]

for num in numbers: 
    if num > max_value:
        max_value = num

    print(f"Maximum value: {max_value}")


def find_min(numbers):
    i = 1
    min_value = numbers[0]

    while i < len(numbers):
        if numbers[i] < min_value:
            min_value = numbers[i]
        i += 1

    return min_value

numbers = [10, 4, 23, 7, 15]
print(f"Minimum value: {find_min(numbers)}")

def find_max(numbers):
    i = 1
    max_value = numbers[0]

    while i < len(numbers): 
        if numbers[i] > max_value:
            max_value = numbers [i]
        i += 1

    return max_value

numbers = [10, 4, 23, 7, 15]
print(f"Maxiumum value: {find_max(numbers)}")


def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10 
        total += digit 
        n = n // 10
    return total 
    
print(sum_of_digits(2468))



result = secret_code(111607) # takes the last digit and places it at the front of the code (71160)
print(f"The result of Secret Code (5.4) with secret_code = {111607} is {result}.")
