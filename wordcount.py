word=1
msg=input("Enter any message: ")
i=0
while i<len(msg):
	if msg[i]==" ":
		word=word+1
	i=i+1
print("There are",(word),"words.")
