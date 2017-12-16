a=raw_input()
string=a[:]
b=str(string)[::-1]
if(a==b):
	print("palindrome")
else:
	print("not an palindrome")
