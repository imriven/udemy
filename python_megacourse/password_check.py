correct_password = "python123"
name = input("Please enter your name: ")
surname = input("Please enter your last name: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Try again: ")

message = "Hi %s %s you are now logged in" % (name, surname)
print(message)


# print("Hi %s you are now logged in" % name)



"""

print("Hi" name, "You are now logged in")

This works too but is not the preferred way to do this.
We want to use string formatting and we can put it into a variable to print it out

"""