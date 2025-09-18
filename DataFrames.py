import pandas as pd

data =[]
n=int(input("Enter No. of data to add : "))
for i in range(n):
	print(f"Data for {i+1} element :")
	nm=input("Name of City :")
	Area=input("Name of Area :")
	pop=int(input("Population :"))
	data.append([nm,Area,pop])
columns = ["Name", "Area", "Poppulation"]

df = pd.DataFrame(data, columns=columns)
print(df)
