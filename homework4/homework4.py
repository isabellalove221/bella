# # --- Homework 4 List and Dicitionaries ----

# # Lists
# # 3.1 List Operations
favorite_foods = ["pizza", "sushi", "sandwich", "peach", "fries"]
print(favorite_foods[1])

# #  I encountered this error
# # Traceback (most recent call last):
# #   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 1, in <module>
# #     list = [pizza, sushi, sandwich, peach, fries]
# #             ^^^^^
# # NameError: name 'pizza' is not defined

# # I forgot to put "" around my strings. I fixed it by adding quotation marks. 

print(favorite_foods[-1])
favorite_foods.append("steak")
print(favorite_foods)

favorite_foods.insert(0, "apple")
print(favorite_foods)

favorite_foods.remove("sandwich")
print(favorite_foods)

# # I encountered this error
# # Traceback (most recent call last):
# #   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 20, in <module>
# #     favorite_foods.remove(2)
# # ValueError: list.remove(x): x not in list
# # I tried to use 2 to remove the third item instead of listing the actual item, I fixed this by replacing 2 with "sandwich"

print(len(favorite_foods))

for foods in favorite_foods:
    print(foods.upper())

# # I encountered this error 
# # Traceback (most recent call last):
# #   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 33, in <module>
# #     favorite_foods.upper(foods)
# # AttributeError: 'list' object has no attribute 'upper'
# # I tried to print all items in uppercase using favorite_foods.upper(foods) and then print(foods) which did not work and I had to fix my syntax
# # I corrected this by correcting my syntax to  print(foods.upper()) after the for loop

first_last_food = [favorite_foods[0], favorite_foods[-1]]
print(first_last_food)

# # I encountered this error
# # Traceback (most recent call last):
# #   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 43, in <module>
# #     first_last_food = [favorite_foods[0,-1]]
# # TypeError: list indices must be integers or slices, not tuple
# # I tried to use first_last_food = [favorite_foods[0,-1]] 
# # I corrected it to first_last_food = [favorite_foods[0], favorite_foods[-1]]

if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!")

# # 3.2 Slicing and Striding 
numbers = list(range(21))
print(numbers)

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    return lst[::-2]

step1 = get_first_15(numbers)
print(step1)

step2 = get_every_5th(step1)
print(step2)

step3 = reverse_and_stride(step2)
print(step3)

# # 3.3 Nested List 
# # 3.3.1 Nested List Opperations
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(lst):
    total = 0
    for row in lst:
        total += sum(row)
    return total

print(sum_nested(numbers))

# I encountered this error
# Traceback (most recent call last):
#   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 97, in <module>
#     print(sum_nested(numbers))
#   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 95, in sum_nested
#     total += sum(row)
# UnboundLocalError: local variable 'total' referenced before assignment
# I got this error because total was not defined before I tried to use it 
# I fixed it by adding total = 0 

# 3.4 Create a 5.5 List
def create_5x5():
    result = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        result.append(row)
    return result

matrix = create_5x5()
print(matrix)

def replace_multiples_of_3(lst):
    new_list = []
    for row in lst:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_list.append(new_row)
    return new_list

# I encounterd an error, my function was not returning anything
# My return fuction was incorrectly indented 
    
updated_matrix = replace_multiples_of_3(matrix)
print(updated_matrix)

def sum_not_question(lst):
    total = 0
    for row in lst:
        for item in row:
            if item != "?":
                total += item
    return total

result = sum_not_question(updated_matrix)
print(result)


# 4 Dictionaries
# 4.1 Dictionary Opperations 
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])

ages["Mira"] = 100
print(ages["Mira"])

# I encountered this error 
#   File "/Users/bellalovee/python_decal_fall25/bella/homework4/homework4.py", line 171
#     ages("Mira") = 100
#     ^
# SyntaxError: cannot assign to function call
# I used () to print the function instead of []

ages["Milana"] = 52
print(ages)

del ages["Mariam"]
print(ages)

for name, age in ages.items():
    print(name, "is", age, "years old")

