f=open("Script.py","r")
f1=open("copyScript.py","w")

data=f.readlines()

for i in data:
	if i[0]=="#" or i[0]=="":
		continue
	else:
		f1.write(i)

f.close()
f1.close()

