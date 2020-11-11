# Chapter 6: Dictionaries
# dictionary is a set of key-value pairs
# keys must be unique

#empty dictionary
dict = {}
print(f"dict = {dict}")

dict = {'key01':'value01'}
print(f"dict = {dict}")

dict = {
    'key01':'value01',
    'key02':'value02',
    'key03':'value03'
}
print(f"dict = {dict}")

dict = {
    'key01':'value01',
    'key01':'value02',
    'key01':'value03'
}
print(f"dict = {dict}")

num_list = [2, 3, 6, 10]
kids = {
    'child1':'Cerrissa',
    'child2':'Ailsa',
    'child3':'Jaida'
}
dict = {
    'name':'rick', #key: string, value: string
    'age':29, #key: string, value: integer
    'height':'510', #key: string, value: string
    'is_married':True, #key: string, value: boolean
    'jump_record':num_list, # key: string, value: list
    'children':kids # key: string, value: dictionary
}
print(f"dict = {dict}")

print(f"Rick's age: {dict['age']}")
print(f"Rick's children: {dict['children']}")

dict['sports'] = 'krav maga'
print(dict)
print(f"Rick practices: {dict['sports']}")