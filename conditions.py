# input temperature from user and cast it to an integer
temp= int(input("Please enter the current temperature: "))
# test all cases and output correct statement
if (temp > 90 ):
    print("Wear Shorts")
elif (temp > 70 ):
    print("Short sleeves are fine")
elif (temp > 50):
    print("Wear a jacket")
elif (temp > 32):
    print("Wear a heavy coat")
else:
    print("Stay Inside")
