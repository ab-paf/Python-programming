name = "Abel Mengistu"
name[0]
print(name[3])
print(name[len(name)-1])
print(name[-1])


data = input("Hi there!")

for index in range (len(data)):
    print(index, data[index])

name = "myfile.txt"
name[0:]
print(name[0:1])
print(name[:len(name)])
print(name[-3:])

fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
    if ".exe" in fileName:
        print(fileName)