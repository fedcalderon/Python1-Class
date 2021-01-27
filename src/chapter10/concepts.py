# CH 10, working with files

work_path = '/Users/federicocalderon/PycharmProjects/Python1-Class/src/scratch_files/'

def demo_getpi():
    print(get_pi())
    pi = get_pi()
    pi2 = pi.lstrip()
    # 2*pi*r^2
    radius = 5
    circ = 2 * float(get_pi().strip()) * radius * radius
    print(f"circum = {circ}")

def get_pi():
    """This function reads a file containing the number pi"""
    try:
        with open(work_path + 'pi_digits.txt') as file:
            pi = file.read()
    except FileNotFoundError:
        print("File or directory not found")
    return pi

def get_states():
    """This function reads a file containing a list of states, line by line"""
    try:
        with open(work_path + 'states.txt') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File or directory not found")

def read_file_to_list():
    filename = work_path + 'states.txt'
    with open(filename) as file_object:
        lines_list = file_object.readlines()

    print(type(lines_list))
    for line in lines_list:
        print(line.strip())

def work_with_file_contents():
    filename = work_path + 'states.txt'
    concat_states = ''
    try:
        with open(filename) as file_object:
            lines_list = file_object.readlines()
    except FileNotFoundError:
        print("File or directory not found")

    for line in lines_list:
        concat_states += line.strip()

    print(concat_states)
    print(type(concat_states))
    return concat_states

def write_to_files():
    """This function writes data to a file"""
    filename = work_path + 'generated_file.csv'
    file_contents = work_with_file_contents()
    try:
        with open(filename, 'w') as file_object:
            file_object.write(file_contents)
    except FileNotFoundError:
        print("File or directory not found")

def append_to_files():
    """This function appends data to an existing file"""
    filename = work_path + 'generated_file.csv'
    file_contents = get_pi()
    try:
        with open(filename, 'a') as file_object:
            file_object.write('\n')
            file_object.write(file_contents)
    except FileNotFoundError:
        print("File or directory not found")

def try_block():
    x=5
    y=99
    try:
        tot = x / y
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    else:
        print(tot)

########################
# MAIN PROGRAM
########################
#demo_getpi()
#get_states()
#read_file_to_list()
#work_with_file_contents()
#write_to_files()
append_to_files()
#try_block()