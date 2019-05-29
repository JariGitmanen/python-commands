def change(msg):
    i=0
    string=""
    while i<len(msg):
        if ord(msg[i])>=65 and ord(msg[i])<=90:
            string = string + chr((ord(msg[i])+32))
        else:
            if ord(msg[i])>=97 and ord(msg[i])<=122:
                string = string+ chr((ord(msg[i])-32))
            else:
                if ord(msg[i])>=48 and ord(msg[i])<=57:
                    string = string + str(int(msg[i])*2)            
                else:
                    string = string + msg[i]
        i=i+1
    return string

string = input("Enter combination: ")
print(string,"now reads as",change(string))