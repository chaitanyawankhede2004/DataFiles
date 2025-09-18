import pandas as pd

filename = 'students.csv'

data = []
for i in range(2):
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    data.append([name, student_id])

df = pd.DataFrame(data, columns=['Name', 'ID'])
df.to_csv(filename, index=False)

print("Student details added successfully!")

df_read = pd.read_csv(filename)
for index, row in df_read.iterrows():
    for item in row:
        print(item, end="\t")
    print("\n")

