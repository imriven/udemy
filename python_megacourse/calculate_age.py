year = int(input("What year were you born: "))

def calculate_age(year):
    age = 2018 - year
    return age

your_age = calculate_age(year)

print("You are " + str(your_age))