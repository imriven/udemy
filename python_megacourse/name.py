temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return False
    else:
        f = c* 9/5 + 32
        return f

myfile = open("resources/temps.txt", "w")


for t in temperatures:
    temp = c_to_f(t)
    if temp != False:
        print(str(temp), file=myfile)
    
myfile.close()