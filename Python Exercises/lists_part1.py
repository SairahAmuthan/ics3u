print("\nExercise 1 ")
careers = ["programmer", "pediatrician", "graphic designer", "architect"]
print(careers)
print(careers.index("graphic designer"))
print(len(careers))
print("graphic designer" in careers)
careers.append('doctor')
careers.insert(0,'Designer')

for career in careers:
   print(career.title())

print(len(careers))

print("\n\nExercise 2 ")
fav_subjects = []
fav_subjects.append("ICS")
fav_subjects.append("English")
fav_subjects.append("Science")
fav_subjects.append("History")

print(len(fav_subjects))
print(fav_subjects[0])
print(fav_subjects[-1])

print("\n\nExercise 3 ")
computer_parts = ["Hard drive", "CPU", "Motherboard", "RAM", "ROM", "GPU"]
print("\nHere is the list in its original order:")
for computer_part in computer_parts:
    print(computer_part.title())

print("\nHere is the list in alphabetical order:")
for computer_part in sorted(computer_parts):
    print(computer_part.title())

print("\nHere is the list in its original order:")
for computer_part in computer_parts:
    print(computer_part.title())

print("\nHere is the list in reverse alphabetical order:")
for computer_part in sorted(computer_parts, reverse=True):
    print(computer_part.title())

print("\nHere is the list in its original order:")
for computer_part in computer_parts:
    print(computer_part.title())

print("\nHere is the original list in reverse order:")
computer_parts.reverse()
for computer_part in computer_parts:
    print(computer_part.title())

print("\nHere is the list in its original order:")
computer_parts.reverse()
for computer_part in computer_parts:
    print(computer_part.title())

print("\nHere is the list permanently in alphabetical order:")
computer_parts.sort()
for computer_part in computer_parts:
    print(computer_part.title())

print("\nHere is the list permanently in reverse alphabetical order:")
computer_parts.reverse()
for computer_part in computer_parts:
    print(computer_part.title())


print("\n\nExercise 4")
numbers = [1,3,4,5,3,2,]
print("\nThis is the list in its original order")
for number in numbers:
    print(number)

print("\nHere is the list in increasing order:")
for number in sorted(numbers):
    print(number)

print("\nThis is the list in its original order")
for number in numbers:
    print(number)

print("\nThis is the list in decreasing order")
for number in sorted(numbers, reverse=True):
    print(number)

print("\nThis is the list in its original order")
for number in numbers:
    print(number)
    
print("\nThis is the list reversed from its original order")
numbers.reverse()
for number in numbers:
    print(number)

print("\nThis is the list in its original order")
for number in numbers:
    print(number)

print("\nThis is the list permanently in increasing order")
numbers.sort()
for number in numbers:
    print(number)

print("\nThis is the list permanently in decreasing order")
numbers.reverse()
for number in numbers:
    print(number)
