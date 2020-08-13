# Removing Items by position:
# You can use the "del" command to remove an item from a list
# if you know it's specific position

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove the first dog from the list.
del dogs[0]

print(dogs)

 #Removing items by value:
 # Using the "remove()" function, you can remove an item from a list
 # that has a specific value

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

 # Remove australian cattle dog from the list.
dogs.remove('australian cattle dog')

print(dogs)

 # HOWEVER, this function only removes the first occurence of that value
 # if the value is in multiple items in you list, it will only delete the first

letters = ['a', 'b', 'c', 'a', 'b', 'c']
 # Remove the letter a from the list.
letters.remove('a')

print(letters)


 #Popping items from a list:
 # The ".pop()" function is a cool way programmers can take an item
 # out of a list, use it, and then delete it from the list
 # note: the default for the ".pop()" function with empty parathesis is
 # to remove the last item in a list

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
last_dog = dogs.pop()

print(last_dog)
print(dogs)


 # HOWEVER, you can add the index of an item to pop that item out of the list
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

first_dog = dogs.pop(0)

print(first_dog)
print(dogs)


#Exercise:
family = ["vathsala", "amuthan", "nikhil", "shaye"]
cousin = family.pop()
print(family)
print(len(family))

dad = family.pop(2)
print(family)
print(len(family))

del family[1]
print(family)
print(len(family))

family.remove("vathsala")
print(family)
print(len(family))

print("There are no more people in my list")
print(family)


#Slicing a list
# Allows you to create a subset of items in a list, the first number is that we want the last upto where we want but not including that

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']
# Grab the first three users in the list.
first_batch = usernames[0:3]
for user in first_batch:
    print(user.title())

# Grab the first three users in the list ( You do not need to put in 0).
first_batch = usernames[:3]
for user in first_batch:
    print(user.title())

# When you gab items from the list, this DOES NOT affect the original list
# [:] can be used to grab any segment from the list, front, middle, append
# If you want to grab everything until the end do [3:]


# Copying a list
# You can use the slice method to make copies of lists

usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Make a copy of the list.
copied_usernames = usernames[:]
print("The full copied list:\n\t", copied_usernames)

# Remove the first two users from the copied list.
del copied_usernames[0]
del copied_usernames[0]
print("\nTwo users removed from copied list:\n\t", copied_usernames)

# The original list is unaffected.
print("\nThe original list:\n\t", usernames)

#Exercises
alphabet = ["a", "b", "c" , "d" , "e", "f" , "g", "h", "i", "j"]
print(alphabet[:3])
print(alphabet[5:8])
print(alphabet[7:])

fav_foods = ["icecream", "chocolate", "nachos"]
fav_foods_copy = fav_foods[:]

fav_foods_copy.append("pie")
fav_foods_copy.append("cookies")

print("This is the original list: \n\n",fav_foods)
print("This is the copied list: \n\n", fav_foods_copy)


# Numerical lists
# range() function : helps generate long lists of numbers

for number in range(1,11):
    print(number) #it outputs every intergeter upto bu not including the last number

for number in range(1,21,2): #last number can change the "step" value
    print(number)

#for number in list(range(1,1000001)):
    #print(number) You can put all the numbers within a list

#min(), max(), and sum() functions

ages = [23, 16, 14, 28, 19, 11, 38]

youngest = min(ages) #finds the minimum value
oldest = max(ages) #finds the maximum value
total_years = sum(ages) #finds the total of all the numbers

print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) + " years worth of life experience.")

#Exercises

for number in list(range(1,21)):
    print(number)

for number in list(range(1,1000001)):
    print(number)

wallets = [67,88,147,200,30]
fattest_wallet = max(wallets)
skinniest_wallet = min(wallets)
total_sum = sum(wallets)
print("\nThe fattest wallet has $",fattest_wallet, " value in it.")
print("\nThe skinniest wallet has $",skinniest_wallet, " value in it.")
print("\nAll together, these wallets have $",total_sum, " value in them.")

#Slicing strings
# We can acess any character in a string by knowing its index
message = "Hello World!"
first_char = message[0]
last_char = message[-1]

print(first_char, last_char)

# We can also take slices from strings
message = "Hello World!"
first_three = message[:3]
last_three = message[-3:]

print(first_three, last_three)

# Finding substrings
# you can use the "in" keyword to cheack if a substring is in a string
# returns true or false

message = "I like cats and dogs."
dog_present = 'dog' in message
print(dog_present)

# you can use the find() function, to see at what index a
# substring starts in a string, HOWEVER it will only find
# the first occurence

message = "I like cats and dogs, but I'd much rather own a dog."
dog_index = message.find('dog')
print(dog_index)

# if you want the last occurence of a substring,
# you can use the rfind() function

message = "I like cats and dogs, but I'd much rather own a dog."
last_dog_index = message.rfind('dog')
print(last_dog_index)


# Replacing substrings
# You can use the replace() fucntion to replace a substring with another
# substring, within the parathesis (string you would like to replace , what you would like to replace it with)

message = "I like cats and dogs, but I'd much rather own a dog."
message = message.replace('dog', 'snake') #needs to be stored within a variable
print(message)


# Counting substrings
# You can use the "count()" function to see how many times a substring is in a string
message = "I like cats and dogs, but I'd much rather own a dog."
number_dogs = message.count('dog')
print(number_dogs)

# You can also use this for lists, and see how many times a substring is in that list
list = ["a","b","a","c"]
count = list.count("a")
print(count)

# Splitting strings
# You can split strings, the default is it will split strings by the space into a list
message = "I like cats and dogs, but I'd much rather own a dog."
words = message.split(' ')
print(words)

animals = "dog, cat, tiger, mouse, liger, bear"

# Rewrite the string as a list, and store it in the same variable
animals = animals.split(',')
print(animals)
