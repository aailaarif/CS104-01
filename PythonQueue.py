names=[]
for x in range(0,10):
    acceptedName= input("Please enter a name: ")
    names.append(acceptedName)
print (names)
for x in range(len(names)):
    print(names.pop(0))
print (names)



