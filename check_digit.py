# Take +ve integer input and tell if it is a four digit num or not.
user_input = int(input("enter any positive num "))

if (user_input >= 1000  and user_input < 9999):
    print("this is 4 digit num")
else:
    print("not")