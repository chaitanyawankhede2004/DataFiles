f=open("countOfChar.py","r")
data=f.read()
f.close()
cnt=0
sr=input("Enter charecter to search :")
for i in data:
	if i==sr:
		cnt+=1

print(f"No of {sr} in database is {cnt}")
