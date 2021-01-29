file=open("D:\intern.txt","r")
arr=file.read()
temp=arr.split("\n")
for x in temp:
    print(x)