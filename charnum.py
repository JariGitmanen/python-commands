char=0
msg=input("Enter any message: ")
i=0
search=input("What are you looking for?: ")
while i<len(msg):
	if msg[i]==search:
		char=char+1
	i=i+1
print("There are",char,"of the letter","'",search,"'","in this sentence.")
