f=open("NewFile.txt",'w')

str1=input("Enter Data to add in File:")

f.write(str1)

f.close()

f=open("NewFile.txt")
print(f.readline())
print(f.readline())
f.close()
