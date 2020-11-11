# Chapter 4 - Working with Lists

#define a list variable
#               0        1        2           3       4       5       6        7
magicians = ['alice', 'david', 'carolina', 'ezra', 'sasa', 'jacob', 'fed', 'jazmin']
# use the print() built in function to show values
#print(f"Item 0 = {magicians[0]}")
#print(f"Item 1 = {magicians[1]}")
#print(f"Item 2 = {magicians[2]}")
#print(f"Item 3 = {magicians[3]}")
#print(f"Item 4 = {magicians[4]}")
#print(f"Item 5 = {magicians[5]}")
#print(f"Item 6 = {magicians[6]}")
#print(f"Item 7 = {magicians[7]}")
#print(f"Item 8 = {magicians[8]}")

print(f"The size of the magicians list is: {len(magicians)}")

# create a counter variable
index = 0

# For loops
# for each <variable name> in <list>:
for name in magicians:
    print(f"Item {index + 1} = {name}")
    # increment the index
    index = index + 1

#while <condition -> expression evaluate to either true or false>:
    #code...
print("\n*************************\n")
index2 = 0
while index2 != -1:
    list_size = len(magicians)
    if index2 < list_size:
        print(f"Item {index2 + 1} = {magicians[index2]}")
        index2 += 1
    else:
        index2 = -1

print("Program ended.")

print("\n*************************\n")

def_range = list(range(1,6))
for value in def_range:
    print(value)
print("\n*************************\n")


for value in range(1,6):
    print(value)
print("\n*************************\n")

for value in range(1,6,3):
    print(value)