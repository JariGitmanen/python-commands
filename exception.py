try:
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    result = no1/no2
    print("The result is ",result)
except ValueError:
    print("Please enter digits only.")
except ZeroDivisionError:
    print("Unable to divide by zero.")