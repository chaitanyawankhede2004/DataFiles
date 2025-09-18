import pandas as pd

data =[]
n=int(input("Enter No. of data to add : "))
for i in range(n):
	print(f"Data for student {i+1} :")
	nm=input("Name :")
	roll=int(input("Roll No. :"))
	data.append([nm,roll])
columns = ["Name", "Roll No."]

df = pd.DataFrame(data, columns=columns)
print(df)
