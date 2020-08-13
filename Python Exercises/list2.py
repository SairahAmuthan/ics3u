#Exercise 1
print("\nExercise 1")
sentence = "Hi, this is my sentence"
for letter in sentence:
    print(letter)

#Exercise 2
print("\nExercise 2")
sentence = "Hi, this is my sentence"
sentence = list(sentence)
print("\n",str(sentence))

# or if its split up by words

sentence = "Hi, this is my sentence"
sentence = sentence.split()
print("\n",str(sentence))

#Exercise 3
print("\nExercise 3")
sentence = "I really like dogs"
first_char = sentence[:5]
middle_char = sentence[7:12]
last_char = sentence[12:17]

print("\nThe sentence is: ", sentence)
print("\nThe first five characters in the sentence are: ", str(first_char))
print("\nMiddle characters in the sentence are ", str(middle_char))
print("\nThe last five characters in the sentence are ", str(last_char))

#Exercise 4
sentence = "Today I learned Python and it was very cool, Python is a fun language"
response = "Python" in sentence
print("\nExercise 4")
print("\na)\n")
print("This is the sentence: \n", sentence)

print("\nb)")
print("\nIs 'Python' in this sentence: ", response)

print("\nc)")
first_found = sentence.find("Python")
print("\n'Python' is found at index: ", str(first_found))

print("\nd)")
last_found = sentence.rfind("Python")
print("\n'Python' is found last at index: ", str(last_found))

print("\ne)")
count = sentence.count("Python")
print("\n'Python' is found ", str(count)," times in this sentence")

print("\nf)")
sentence = sentence.split()
for word in sentence:
    print(word)
