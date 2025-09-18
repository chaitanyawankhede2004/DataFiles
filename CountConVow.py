def createFile():
    with open("StudentData.txt", 'a') as f: 
    	nm = input("Enter Name: ")
        dept = input("Enter Department: ")
        yr = input("Enter year: ")
        sem = input("Enter Semester: ")
        dataString = f"{nm},{dept},{yr},{sem}\n"
        f.write(dataString)
        print("Data Entered Successfully!")


def PrintData():
    try:
        with open("StudentData.txt", 'r') as f:
            Data = f.read()
            print("Student Data:\n", Data)

            spChar = 0
            con = 0
            vow = 0
            space = 0

            for char in Data:
                if char.isspace():
                    space += 1
                elif char.isalpha():
                    if char.lower() in "aeiou":
                        vow += 1
                    elif char.lower() in "bcdfghjklmnpqrstvwxyz":
                        con += 1
                else:
                    spChar += 1 

            print("Number of Consonants:", con)
            print("Number of Vowels:", vow)
            print("Number of Spaces:", space)
            print("Number of Special Characters:", spChar)
    except FileNotFoundError:
        print("Error: StudentData.txt not found.")


createFile()
PrintData()

