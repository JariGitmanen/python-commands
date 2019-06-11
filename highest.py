numbers=[]
while True:
    num=int(input("Enter any number: "))
    if num==0:
        break
    else:
        numbers.append(num)
Highest=numbers[0]
i=1
while i<len(numbers):
    if numbers[i]>Highest:
        Highest=numbers[i]
    i=i+1
print("Highest",Highest)