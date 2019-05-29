def wordcount(message):
    word=1
    i=0
    while i<len(message):
        if message[i]==" ":
            word+= 1
        i+= 1
    return word
A = (input("Enter sentence here: "))
B = (input("Enter sentence here: "))
print("word count: ",wordcount(A))
print("Word count: ",wordcount(B))