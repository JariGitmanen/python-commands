Name=input("Enter your name: ")
Salary=int (input("Enter your salary: £"))
if Salary>2000:
	Tax=Salary*25/100
else:
	Tax=Salary*15/100
NetSalary=Salary-Tax
print("Your name: ",Name)
print("Total Taxed: £",Tax)
print("Your take-home Salary: £",NetSalary)