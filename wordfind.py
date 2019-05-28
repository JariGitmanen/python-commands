word=0
msg=input("Enter any message: ")
search=input("What word are you looking for?: ")
i=0
while i<len(msg):
	if msg[i]==search[0]:
		if msg[i:i+len(search)]==search:
			word=word+1
			i=i+len(search)-1
	i=i+1
print("There are",word,"of the word","'",search,"'","in this sentence.")
