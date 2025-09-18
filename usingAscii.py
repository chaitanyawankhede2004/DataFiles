def createFile():
    f = open("StudentData.txt", 'a')
    nm = input("Enter Name: ")
    dept = input("Enter Department: ")
    yr = input("Enter year: ")
    sem = input("Enter Semester: ")
    dataString = f"{nm},{dept},{yr},{sem}\n"
    f.write(dataString)
    print("Data Entered Successfully!")
def PrintData():
    f = open("StudentData.txt", 'r')
    Data = f.read()
    print("Student Data:\n", Data)
	spChar=0
    con = 0
    vow = 0
    space = 0
    dig=0
    for i in Data:
        if i.isspace():
            space += 1
        elif ord(i):
		    if i.lower() in "aeiou":
		        vow += 1
		    elif i.lower() in "bcdfghjklmnpqrstvwxyz":
		        con += 1
		elif i.isnum():
			dig+=1
		else:
			spChar+=1
    print("Number of Consonants :", con)
    print("Number of Vowels :", vow)
    print("Number of Spaces :", space)
	print("Number of Digits :", dig)	
	print("Number of Spacial :", spChar)
	
createFile()	
PrintData()
	
