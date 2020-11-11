# Chapter 5: If statements

cars = ['audI', 'bMw', 'subAru', 'toYota']

for car in cars:
    if car.lower() == 'bmw':
        print(f"in lower case: {car.lower()}")
        print(car.upper())
    else:
        print(car.title())
print("******************")
print("******************")
age_groups = [16, 21, 9, 33, 42, 2]
for age in age_groups:
    print(f"Current age being evaluated: {age}")
    if (age == 9):
        print("Found age 9!")
    elif age < 9:
        print(f"age ({age}) is less than 9")
    elif (age >= 9) and (age <= 22):
        print(f"age ({age}) is greater than 9")
    else:
        print(f"{age} is not applicable")

print("******************")
for age in age_groups:
    print(f"Current age being evaluated: {age}")
    if (age == 9):
        print("Found age 9!")
    if age < 9:
        print(f"age ({age}) is less than 9")
    if (age >= 9) and (age <= 22):
        print(f"age ({age}) is greater than 9")
    else:
        print(f"{age} is not applicable")
print("******************")
print("******************")
print("check if 30 is not in the list")
if 30 not in age_groups:
    print(f"30 is not in age_groups")

##################################
# Functions
##################################
def find_topping(topping):
    for available_topping in available_toppings:
        if topping == available_topping:
            return topping


available_toppings = ['mushrooms', 'olives', 'anchovies', 'chicken', 'pepperoni', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    #if requested_topping in available_toppings:
    topping = find_topping(requested_topping)
    if requested_topping == topping:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, {requested_topping} is not available")


####### Dictionaries
# Key: unique
dictionary = { 'key1' : 'value1',
               'key2' : 'value2',
               'key3' : 'value3',
               'key4' : 'value4',
               'key5' : 'value5'}
print(dictionary)

# If keys are the same, the last key will be used and all duplicated discarted.
dictionary2 = { 'key1' : 'value1',
               'key1' : 'value2',
               'key1' : 'value3',
               'key1' : 'value4',
               'key1' : 'value5'}
print(dictionary2)
