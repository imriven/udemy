myfile = open("resources/core.txt")
# takes file and enables it to be read by python
content = myfile.read()
# variable storing file as string
myfile.close()
# close the file when it's no longer in use. Otherwise memory being used can add up
print(content)
#print the string