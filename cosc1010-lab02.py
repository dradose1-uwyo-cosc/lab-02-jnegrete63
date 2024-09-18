# Jose F. Negrete Oseguera
# UWYO COSC 1010
# Submission Date 09/17/24
# Lab 02 
# Lab Section:11
# Sources, people worked with, help given to: Lab TA
# once i started to code it is not as intimidating
# comments
# here

Message_1 = "Hello week 3 of fall class 2024"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, cosc1010")

# Assign the string above to a variable named hello_message and print that variable
hello_message = "Hello, cosc1010"
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
msg_cj = "cowboy joe"
print(msg_cj)

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`

uwyo = "University of wyoming"
uw_founded = "1886"

print(f"The {uwyo} was founded in {uw_founded}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings

x = 5
y = 10
print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 

first_name = "Jose"
midle_name = "Fabian"
Last_name = "Negrete Osegeura"
Space = " "

print(f"{first_name}{Space}{midle_name}{Space}{Last_name}")