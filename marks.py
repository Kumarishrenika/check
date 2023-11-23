marks = int(input("enter the marks: "))
# if marks are between 81 and 100 ---> 
if (marks > 80):
    print("Excellent")
# if marks are between 60 and 80 ---> 
elif (marks > 60):
    print("Good")
# if marks are between 41 and 60  ---> 
elif (marks > 40 ):
    print("Average")
else:
    print("Fail")
