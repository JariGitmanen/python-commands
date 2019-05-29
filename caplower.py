A = input("Enter any letter: ")
if ord(A)>=65 and ord(A)<=90:
    print(chr(ord(A)+32))
else:
    print(chr(ord(A)-32))