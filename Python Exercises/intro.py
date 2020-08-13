#Intro to Python

#VARIABLE

message = "Hello Python World"
print(message)

message = "Python is my favourite language"
print(message)

#Naming Conventions
# lowercase variable names, starting with a letter
# Do not use a number as the first character
# YOU CANNOT USE PYTHON KEYWORDS

#import keyword
#Imports a module that has all the KEYWORDS
#print(keyword.kwlist)

#If you try and use a KEYWORDS
# pass = False - returns "Syntax error"
# for = "me" - returns "Syntax error"
# lambda = "greek" - returns "Syntax error"

message= "Share Python with the world!"
# print(mesage) will return "Name Error"

#Variable: a place to store data or values
# in line 26, message is the variable and it stores "Share Python with the world"

red = 5
blue = 10
print(blue,red)

yellow = red
print(yellow,red, blue)

red = blue
print(yellow, red, blue)

#Variable Exercises

message = "Hi I'm Sairah"
print(message)
message2 = "Whats your name?"
print(message2)

one = 1
two = 1
three = 3

print(one, two, three)

#Example 3.1 - Both strings will print off the same

my_string = "This is a double-quoted string."
my_string = 'This is a single-quoted string.'

#Example 3.2

quote = "Ms.Maquiling once said, 'Use your voice.'"
print(quote)

#Example 3.3
# ".title()" takes the first letter of a string and converts it to uppercase

first_name = 'moana'
print(first_name)
print(first_name.title())


#Example 3.4
print(first_name.upper())
# ".upper" changes every letter into uppercase


#Example 3.5
first_name = "MoanA"
print(first_name.lower())
# ".lower" changes every letter into uppercase


#COMBINING/REPEATING STRINGS (CONCATENATION)
#Example 3.6
#Use the addition sign (+) to add strings together
first_name = "taika"
last_name = 'waititi'
full_name = first_name + ' ' + last_name
print(full_name.title())

#Example 3.7
# The * symbol can repeat a string x amount of times
print("cycle, " * 10)


#Example 3.8
# You use the len() function to find out the length of a string

print(len("Sairah!"))


#Example 3.9
question = "What did you have for lunch?"

#answer = input(question)
#print("You had " + answer + "! That sounds delish!")
#print(len(answer))

#Example 3.10
# "\t" makes a tab appear in the string
print("Hello everyone!")
print("\tHello everyone!")
print("Hello \teveryone!")

#Example 3.11
# "\n" makes a newline appear in a string
print("Hello everyone!")
print("\nHello everyone!")
print("Hello \neveryone!")
print("\n\n\nHello everyone!")


#Exercises
first_name = "sairah"
print(first_name)
print(first_name.title())
print(first_name.upper())

first_name = "Sairah"
last_name = "Amuthan"
full_name = first_name + " " + last_name
print(full_name.title())

first_name = "Michelle"
last_name = "Obama"
full_name = first_name + " " + last_name
print(full_name.title() + " is amazing!")

string = "12345"
print(string.isnumeric())

array = "Hi i am sairah"
print(array.count("x"))

string = "Shreya, is really cool"
print(string.split("b"))

sentence = "How was your day?"
found = sentence.find("How")
print(found)
