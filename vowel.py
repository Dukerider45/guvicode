vowel=["a","e","i","o","u"]
letter=input()
if(letter.isalpha()):
	if(letter in vowel):
		print ("Vowel")
	else:
		print ("Consonant")
else:
	print("invalid")
