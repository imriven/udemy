numbers = [1, 2, 3]
file = open("to_file.txt", "w")
for i in numbers:
     file.write(str(i) + "\n")
file.close()

myfile = open("resources/to_file.txt")
file = myfile.read()
print(file)