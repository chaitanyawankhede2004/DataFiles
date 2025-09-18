f=open("student.txt",'w')

n=int(input("Enter no of students:"))
for i in range(n):
	nm=input("Enter Name")
	dept=input("Enter Department")
	ye=input("Enter year :")
	sm=input("Enter Semister:")
	string="My name is "+nm+". I am in "+dept+" Department " +  ", in "+ye+" year "+sm+" semister."
	f.write(string)
	f.write("\n\n")
	

f.close()

f=open("student.txt")
print(f.read())

f.close()
