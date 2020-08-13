print(0.6 -0.4)
print(0.1/0.3)
print(10/3)

#Combining Numbers and strings

print ("Please give me a number: ")
number = input() #Ths is a string
plusTen = float(number) + 10 #You cannot add strings and numbers, you need the int()

print ("If we add 10 to your number, we get " + str(plusTen))
print ("If we add 10 to your number, we get %s" % plusTen)
print ("If we add 10 to your number, we get {0}".format(plusTen))

plusTwenty = float(number) + 20
print("We add 10 and 20 to your number, resulting in {0} and {1}" .format(plusTen, plusTwenty))
