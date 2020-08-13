# If and Else statements

desserts = ["ice cream", "chocolate", "apple crisp", "cookies"]
favourite_dessert = "chocolate"
for dessert in favourite_dessert:
    if dessert == favourite_dessert:
        print("%s is my favourite dessert" % dessert.title())

    else:
        print("I like %s a bit" % dessert)

print("5 == 5", 5 == 5)
print("5 == 5.0", 5 == 5.0)
print("'5' == str(5)", '5' == str(5))

users = ["gina"]
if len(users) > 4:
    print("We have several users")

elif len(users)> 10:
    print("We have many users")

else:
    print("We need more users")

user_input = input("Enter a series of words seperated by a space")
word_list = user_input.split()
vowel_count = []

for word in word_list:
    for letter in word:
        if letter == "a":
            vowel_count.append("a")

        elif letter == "e":
            
