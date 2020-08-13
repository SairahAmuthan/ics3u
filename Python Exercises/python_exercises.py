# Sairah Amuthan
#Exercise 1
print("\nExercise 1: \n")
pay_per_hour = 13.15
hours_worked = int(input("How many hours has the student worked "))
total_pay = 13.15*hours_worked
round(total_pay,2)
print("The student has worked ", str(hours_worked), " hours and have earned $",total_pay)

#Exercise 2
print("\nExercise 2: \n")
string = input("Enter a string ")
number = int(input("Enter a number "))
new_string = string + str(number)
print(new_string * number)

#Exercise 3
print("\nExercise 3: \n")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
fav_number = input("Enter your favourite number: ")
first_name = first_name.lower()
last_name = last_name.upper()
fav_number = fav_number.title()

#Option 1
print("\nHello " + first_name.title() + " " + last_name.title() + "?")

#Option 2
print("Would you like to be called ", first_name, "?")

#Option 3
print("Or would you like to be called %s ?" % last_name)

#Option 4
print("Or maybe {0}?".format(fav_number) )
