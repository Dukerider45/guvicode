a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if(a!=b and a!=c and b!=c):

	if(a>b and a>c):
	
		print(a)

	elif(b>a and b>c):		

		print(b)

	else:
	
		print(c)
elif (a==b):
	if(b>c):
		print(b)
	else:
		print(c)
elif (a==c):
	if(b>c):
		print(b)
	else:
		print(c)
else:
	if(a>b):
		print(a)
	else:
		print(b)
