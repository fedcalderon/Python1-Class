# While loops and user input
# ********************************************************************************
#                   VARIABLES AREA
# ********************************************************************************

users = []
user_counter = 0

# ********************************************************************************
#                   FUNCTION DEFINITION AREA
# ********************************************************************************
def while_loops_principles():
    """
    This function examines the behavior of while loops and user input
    :return: None
    """
    # exit = 1 means exit the program, 0 means keep going
    exit = 0
    while(exit == 0):
        message = input("Tell me your name: ")
        print(f"Hello {message}!")

        message = input("Tell me your age: ")
        print(f"You are {message} years old!")

        message = input("Want to quit? (Y, N):")
        if message == 'Y':
            exit = 1
def show_help():
    """
    This function shows the user information about this program.
    :return: None
    """
    print("Thank you for purchasing this product.")
    print("We are learning about user input and while loops.")
def collect_user_data():
    """
    This function collects user data.
    :return: None
    """

    # exit = 1 means exit the program, 0 means keep going
    exit = 0
    while (exit == 0):
        user = {
            'first_name': '',
            'last_name': '',
            'age': 0,
            'can_vote': ''
        }

        fist_name = input("Hello!\nType your first name: ")
        last_name = input("Type your last name: ")
        age = input("Type your age: ")

        user['first_name'] = fist_name
        user['last_name'] = last_name
        user['age'] = age
        # test
        print(f"The data type of age is: {type(age)}")

        if int(age) >= 18:
            user['can_vote'] = 'Yes'
        else:
            user['can_vote'] = 'No'

        users.append(user)

        message = input("Want to quit? (Y, N):")
        if message == 'Y':
            exit = 1

def print_users():
    for user in users:
        for k, v in user.items():
            print(f"First name: {user['first_name']}")
            print(f"Last name: {user['last_name']}")
            print(f"Age: {user['age']}")
            print(f"Can vote? {user['can_vote']}")

# ********************************************************************************
#                   MAIN PROGRAM
# ********************************************************************************
# Function calls
while_loops_principles()
show_help()
collect_user_data()
print_users()
print("Out of the loop and exiting the program")