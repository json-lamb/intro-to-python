# This is a single-line comment in Python

'''
This is a block comment.
You can comment multiple lines.
''' 

print('Hello, World!')
# This line defines a function called print_hello_world
def print_hello_world():
    # This line prints the "Hello, World!" message
    print("Hello, World!")


# These lines create variables of different data types
string_variable = "This is a string"  # String data type
integer_variable = 42  # Integer data type
float_variable = 3.14  # Float data type
boolean_variable = True  # Boolean data type

# This line creates a list with elements of different data types
list_variable = [string_variable, integer_variable, float_variable, boolean_variable]

# This line defines a function called print_variables that takes a list as input
def print_variables(variable_list):
    # This for loop iterates over the elements in the variable_list
    for variable in variable_list:
        # This line prints the current variable's value.
        print(variable)
        print(variable, type(variable))
        # This line prints the current variable and its data type, and formats them into a string.
        # print("Value: {} - Data type: {}".format(variable, type(variable)))

# This line calls the print_hello_world function
print_hello_world()

# This line calls the print_variables function with the list_variable as an argument
print_variables(list_variable)

# This line pauses the script and waits for the user to press the Enter key before exiting
input("Press Enter to exit.")
