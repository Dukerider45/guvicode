file=open("one.txt","r")
x=file.read()
if(x.isalpha()):
    print(x)
else:
    print(int(x))
