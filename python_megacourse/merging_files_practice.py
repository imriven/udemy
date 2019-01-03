from datetime import datetime

def content_reader(filename):
    with open(filename) as myfile:
        return myfile.read()

file_name_list = ["resources/file1.txt","resources/file2.txt", "resources/file3.txt"]

combine = ""

for i in file_name_list:
    combine = combine + "\n" + content_reader(i) + "\n"

"""
myfile1 = open("resources/file1.txt")
myfile2 = open("resources/file2.txt")
myfile3 = open("resources/file3.txt")

content1 = myfile1.read()
content2 = myfile2.read()
content3 = myfile3.read()


combine = content1+ "\n" + content2 + "\n" + content3 + "\n"
"""
with open(str(datetime.now())+".txt", "w") as combined_files:
    combined_files.write(combine)

