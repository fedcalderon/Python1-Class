# Chapter 8: functions
# ********************************************************************************
#                   FUNCTION DEFINITION AREA
# ********************************************************************************

def add(x, y):
    sum = x + y
    return sum

def multiply(x, y):
    mult = x * y
    return mult

def sub(x, y):
    sum = x - y
    return sum

def div(x, y):
    divide = x / y
    return divide

def first_try():
    user_input = input("Wanna play? (y, q to quit): ")
    while (user_input != 'q'):
        operation = input("a-Add, s-Subtract, m-Multiply, d-Divide:")
        n1 = input("type your first number: ")
        n2 = input("type your second number: ")

        if operation == 'a':
            result = add(int(n1), int(n2))
            print(f"{n1} + {n2} = {result}")
        elif operation == 's':
            result = sub(int(n1), int(n2))
            print(f"{n1} - {n2} = {result}")
        elif operation == 'm':
            result = multiply(int(n1), int(n2))
            print(f"{n1} * {n2} = {result}")
        elif operation == 'd':
            result = div(int(n1), int(n2))
            print(f"{n1} / {n2} = {result}")
        else:
            print(f"{operation} is not a valid entry! Try again :(")
        #n1_int = int(n1)
        #n2_int = int(n2)
        #result = add(n1_int,n2_int)

        user_input = input("Continue? (y,n, q to quit): ")

def split_html_tag(str_line):
    print("Problem: determine the name of the html tag.")
    print(str_line)
    first_split = str_line.split('>') # Regular Expressions
    print(first_split)
    second_split = first_split[0].split('<')
    print(second_split)
    third_split = second_split[-1].split(' ')
    print(third_split)

    return third_split[0]

# ********************************************************************************
#                   MAIN PROGRAM
# ********************************************************************************
#n1 = "3"
#n2 = 9
#sum = add(n1, n2)
#print(sum)

#first_try()
html_tag_str = '<link rel="dns-prefetch" href="https://github.githubassets.com">'
tag_name = split_html_tag(html_tag_str)
print(f"The tag type is: {tag_name}")

tag_name = '<div data - pjax - replace = "" id = "js-flash-container">'
print(f"The tag type is: {split_html_tag(tag_name)}")

