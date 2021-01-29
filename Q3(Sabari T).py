arr=["Aashrith","Badri","Gaythri",
     "Kiran","Rakesh","Sabari",
     "Omesh","Vamsi"]
file=open("D:\intern.txt","w")
for x in arr:
    file.write("{}\n".format(x))
file.close()         