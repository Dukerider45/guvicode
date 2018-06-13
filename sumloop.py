a,b=raw_input().split(" ")
c=raw_input()
b=int(b)
d=c.split(" ")
sum=0
for i in range(0,b):
	sum=sum+int(d[i])
print (sum)
