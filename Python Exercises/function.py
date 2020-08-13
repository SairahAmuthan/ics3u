# Tuples : are lists that can never change
# You can create a tuple by switching the square brackets with parenthesis

colors = ('red', 'green', 'blue')
print("The first color is: " + colors[0])

print("\nThe available colors are:")
for color in colors:
    print("- " + color)

# colors = ('red', 'green', 'blue')
# colors.append('purple')  this will come out as an error, you cannot change any
# items in a tuple

# Functions: are a set of actions that are grouped together and called upon under one name

# Defining a function:
#       -  Give the keyword def, means you are definig function
#       -  Give your function a name. One that correlates to the function it performs
#       -  The function definition line must end with a ":" (colon)
#       -  Inside the function (INDENTED) is where you right the actions the function should perform

# Using a function:
#       -  To call a function, just write the function name with a parenthesis
#       -  Inside the parenthesis, give the values you want the function to work with

# Basic Examples:

def thank_you(name):
    # This function prints a two-line personalized thank you message.
    print("\nYou are doing good work, %s!" % name)
    print("Thank you very much for your efforts on this project.")

thank_you('Adriana') # calling on the function, in the parenthesis is the value, the function will use
thank_you('Billy')
thank_you('Caroline')

# note: the function must be defined before the function is called
# Second Example:
def show_students(students, message):
   # Print out a message, and then the list of students
   print(message)
   for student in students:
       print(student.title())

students = ['bernice', 'aaron', 'cody']

# Put students in alphabetical order.
students.sort()
show_students(students, "Our students are currently in alphabetical order.")

#Put students in reverse alphabetical order.
students.sort(reverse=True)
show_students(students, "\nOur students are now in reverse alphabetical order.")

# Advantages of using functions:
#       - It saves work, do not need to repeat code
#       - Less chance of having an error in your code, having problems
#       - It is easy to modify a functions behaviour instead of writing new code


# Example: We can just print diverse statements through the function
def show_students(students, message):
    # Print out a message, and then the list of students
    print(message)
    for student in students:
        print("- " + student.title())

students = ['bernice', 'aaron', 'cody']

# Put students in alphabetical order.
students.sort()
show_students(students, "Our students are currently in alphabetical order.")

#Put students in reverse alphabetical order.
students.sort(reverse=True)
show_students(students, "\nOur students are now in reverse alphabetical order.")


# Returing a Value
# Functions can return  a value aside from its original function
# Example: function takes a number, outputs a word

def get_number_word(number):
     # Takes in a numerical value, and returns
     # the word corresponding to that number.
     if number == 1:
         return 'one'
     elif number == 2:
         return 'two'
     elif number == 3:
        return 'three'

# Let's try out our function.
for current_number in range(0,4):
     number_word = get_number_word(current_number)
     print(current_number, number_word)

# HOWEVER, the above function works, but has a logical error:
# add an else statement to let the user know that they must input the numbers within the range

def get_number_word(number):
    # Takes in a numerical value, and returns
    #  the word corresponding to that number.
    if number == 0:
        return 'zero'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    else:
       return "I'm sorry, I don't know that number." #solves the logical error


# Let's try out our function.
for current_number in range(0,6):
   number_word = get_number_word(current_number)
   print(current_number, number_word)

# Exercises
def greeting(name):
    print( "Hello ",name)
    print("How was your day ", name)
    print("Goodbye ", name)

input_name = input("Enter three names,seperated by a coma: ")
names = input_name.split(",")
for name in names:
    greeting(name)


#Fuctions: we use functions to repeat certain steps

#Example t.1

number1 = 3
number2 = 4
number3 = 7

print("Increase all numbers by 10", number1 + 10)
print("Increase all numbers by 10", number2 + 10)  #Has to repeat these lines, better option is to create a function
print("Increase all numbers by 10", number3 + 10)

#Creating a functions
def add_ten(number):
    return number + 10

print("Increase number 1 by 10",add_ten(number1)
print("Increase number 2 by 10",add_ten(number2)
print("Increase number 2 by 10",add_ten(number3)
