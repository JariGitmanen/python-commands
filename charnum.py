char=0
msg=input("Enter any message: ")
i=0
search=input("What character are you looking for?: ")
while len(search)>1:
		search=input("Please only enter one character: ")
while i<len(msg):
	if msg[i]==search:
		char=char+1
	i=i+1
print("There are",char,"of the letter","'",search,"'","in this sentence.")
search=input("would you like to search for anything else?")
