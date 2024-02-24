from email import message


message=input("Write something then I wil show you this:")
print(message)
name=input("Write Name: ")

#1
print(f"Hello,{name}")
#2
print("Hello, {}".format(name))
#3
print("Hello, %s" % name)

#tracking life stage
age=input("Enter ")

import datetime

# Get user's date of birth
dob = input("Enter your date of birth in the format YYYY-MM-DD: ")

# Convert the input to a datetime object
dob = datetime.datetime.strptime(dob, "%Y-%m-%d")

# Get today's date
today = datetime.datetime.now()
print(today)
# Calculate the difference in years
age = today.year - dob.year

# Check if the user has had their birthday this year
if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
    age -= 1

# Store the age in a variable
actual_age = age

print(f"Your age is: {actual_age} years")

if (0<=age and age<=3):
    print("you are Baby")
elif (4<=age and age<=12):
    print("you are Child")
elif (13<=age and age<=19):
    print("you are Teen")
elif (20<=age and age<=34):
    print("you are Adult")
elif (35<=age and age<=64):
    print("you are Middle_Aged")
else:
    print("Senior person")    