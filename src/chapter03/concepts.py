# Python lists

# Define a python list
# <variable name> = []
publix_list = [
    "chicken", # index = 0
    "bread",   # index = 1
    "ham",     # index = 2
    "milk",    # index = 3
    "soda"     # index = 4
]
#print(publix_list[3])
#print(f"The selected item is {publix_list[-1].title()}")


             #  0         1             2          3
#bicycles = [ "trek", "connondale", "redline", "specialized" ]
names = [ "jackson", "ezra", "allen", "marcel" ]
print(f"First name: {names[0].title()}")
print(f"Second name: {names[1].title()}")
print(f"Third name: {names[2].title()}")
print(f"Fourth name: {names[3].title()}")

print("*** Append 3 more names")
names.append("daniel")
names.append("rick")
names.append("patrick")
print(f"Fifth name: {names[4].title()}")
print(f"sixth name: {names[5].title()}")
print(f"seventh name: {names[6].title()}")

print("*** Insert a name in the middle of the list")
names.insert(4, "fed")

print("*** let's sort the list")
names.sort(reverse=True)

print("\n\n")
print(f"First name: {names[0].title()}")
print(f"Second name: {names[1].title()}")
print(f"Third name: {names[2].title()}")
print(f"Fourth name: {names[3].title()}")
print(f"Fifth name: {names[4].title()}")
print(f"sixth name: {names[5].title()}")
print(f"seventh name: {names[6].title()}")
print(f"Eigth name: {names[7].title()}")
print("\n")

print("*** let's pop an item from the list")
popped_item = names.pop(-1)
print(f"popped item: {popped_item}\n\n")

print("\n\n")
print(f"First name: {names[0].title()}")
print(f"Second name: {names[1].title()}")
print(f"Third name: {names[2].title()}")
print(f"Fourth name: {names[3].title()}")
print(f"Fifth name: {names[4].title()}")
print(f"sixth name: {names[5].title()}")
print(f"seventh name: {names[6].title()}")
#print(f"Eigth name: {names[7].title()}")
print("\n")

print("Remove item")
names.remove(names[1])
print("\n\n")
print(f"First name: {names[0].title()}")
print(f"Second name: {names[1].title()}")
print(f"Third name: {names[2].title()}")
print(f"Fourth name: {names[3].title()}")
print(f"Fifth name: {names[4].title()}")
print(f"sixth name: {names[5].title()}")

print("\n*** printing from a loop ***\n")

index_counter = 0
# a taste of chapter 4
# for loop
#foreach <item> in <list>:
for name in names:
    print(f"Name {index_counter + 1}: {name}")
    index_counter = index_counter + 1


#print(bicycles[1].title())
# hard coding
#print(f"Sasa wants her dad to buy her a {bicycles[2].title()} bike!")
#print(f"Ezra wants his dad to buy him a {bicycles[-1].title()} bike!")
#print(f"Jacob wants to buy a {bicycles[0].title()} bike!")

# using a variable for indexing
#bike_index = 3
#name_index = 3

#print(f"{names[name_index].title()} wants to buy a {bicycles[bike_index].title()} bike!")

# modifying a list
#bicycles[0] = "trekk"
#print(bicycles)

# adding elements to the list
#bicycles.insert(2, "walmart")
#print(bicycles)
#bicycles.append("play it again sports")
#print(bicycles)

# deleting
# del + list_name[index]
#del bicycles[1]
#print(bicycles)

# Looping
# foreach <item> in collection:
#for item in bicycles:
#    print(f"Bicycle: {item.title()}")

#for name in names:
#    print(name)