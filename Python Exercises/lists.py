# students = ['bernice', 'aaron', 'cody']
# for student in students:
#     print("Hello, " + student.title() + "!")
#
# #Since lists are a collection of objects, give them a plural name
# #The above goes through each item and prints out the hello message
#
# dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# dog = dogs[0]
# print(dog.title())
#
# #Exercise - Part 1
# #1
# languages = ["python", "java", "c"]
# print("A good programming language is " + languages[0])
# print("An easy program is " + languages[1])
# print("A ver useful program is " + languages[2])
#
# #2
# sports = ["soccer", "basketball", "hockey"]
# print("A really cool sport is " + sports[-1])
# print("A really fun sport is " + sports[-2])
# print("A really hard sport is " + sports[-3])
#
# Lists and Looping

dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
for dog in dogs:
    print('I like ' + dog + 's.')
    print('No, I really really like ' + dog +'s!\n')
print("\nThat's just how I feel about dogs.")


dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
print("Results for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index + 1)
    print("Place: " + place + " Dog: " + dog.title())
