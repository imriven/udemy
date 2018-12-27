a = int(input("What number would you like to use?: "))

b = int(input("What power will we be giving to your number?: "))

def to_the_power(c,d):
    return (c ** d)

answer = to_the_power(a,b)

print( str(a) + " to the power of " + str(b) + " equals " + str(answer))