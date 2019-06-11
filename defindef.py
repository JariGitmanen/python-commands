def operations(day):
    if day==1:
        def fun(a,b):
            c=a+b
            print("Result of addition is ",c)
    if day==2:
        def fun(a,b):
            c=a-b
            print("Result of subtraction is ",c)
    return fun
Minus=operations(2)
Add=operations(1)
Minus(5,2)
Add(554745745742,3646369)