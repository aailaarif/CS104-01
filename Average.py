#initialize variables
average=0
total=0
howManyEntered=0
#input values from user 
howMany=int(input("How many test scores would you like to average? "))
#loop- keep entering test scores until howManyEntered=howMany
while(howManyEntered<howMany):
    testScore=float(input("Enter test score: "))
    total=testScore+total
    howManyEntered+=1
#calculate average and output
average=total/howMany
print("The average for the test scores you entered is: " + str(average))
