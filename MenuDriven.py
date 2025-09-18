def createRecord():
    f = open("EmployeRec.txt", "a")
    f.write("Name\tDepartment\tEmail\tNumber\n")
    for i in range(2):
        nm = input("Enter Name : ")
        dept = input("Enter Department :")
        mail = input("Enter Mail : ")
        num = input("Enter Number : ")
        f.write(f"{nm}\t{dept}\t{mail}\t{num}\n")
    f.close()


def printRec():
    f = open("EmployeRec.txt", "r")
    data = f.readlines()
    for i in data:
        print(i, end="")
    f.close()


def cntofSpecial():
    f = open("EmployeRec.txt", "r")
    cnt = 0
    data = f.read()
    for i in data:
        if not i.isalnum() and not i.isspace():
            cnt += 1
    f.close()
    print(f"Number of special characters: {cnt}")


def copyToOther():
    try:
        f = open("CopyData.txt", "w")
        f1 = open("EmployeRec.txt", "r")
        data = f1.readlines()
        f.writelines(data)
        f.close()
        f1.close()
        print("Data Copied Successfully")
    except Exception as e:
        print(f"Error during copy: {e}")


while True:
    print("\nMenu:")
    print("1. Create Record")
    print("2. Print Record")
    print("3. Count Special Characters")
    print("4. Copy to Other File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        createRecord()
    elif choice == "2":
        printRec()
    elif choice == "3":
        cntofSpecial()
    elif choice == "4":
        copyToOther()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

