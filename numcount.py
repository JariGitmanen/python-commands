Alpha=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
message=input("Enter any message: ")
i=0
while i<len(message):
    Alpha[ord(message[i].upper())-65]+=1
    i=i+1
i=0
while i<=25:
    if Alpha[i]>0:
        print(chr(i+65),"=",Alpha[i])
    i=i+1