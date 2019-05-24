Price = float(input("Enter price of product: £"))
Money = float(input("Enter amount of cash given: £"))
Change = (float(Money)-float(Price))
print("Change due is: £",Change)
print("--------Breakdown--------")
Fifty=Change // 50
Twenty=Change % 50 // 20
Ten=Change % 50 % 20 // 10
Five=Change % 50 % 20 % 10 // 5
Two=Change % 50 % 20 % 10 % 5 // 2
One=Change % 50 % 20 % 10 % 5 % 2 // 1
FiftyP=Change % 50 % 20 % 10 % 5 % 2 % 1 // 0.5
TwentyP=Change % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 // 0.2
TenP=Change % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 // 0.1
FiveP=Change % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 % 0.1 // 0.05
TwoP=Change % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05 // 0.02
OneP=Change % 50 % 20 % 10 % 5 % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05 % 0.02 // 0.01
if Fifty>0:
	print("£50 notes = ",int(Fifty))
if Twenty>0:
	print("£20 notes = ",int(Twenty))
if Ten>0:
	print("£10 notes = ",int(Ten))
if Five>0:
	print("£5 notes = ",int(Five))
if Two>0:
	print("£2 coins = ",int(Two))
if One>0:
	print("£1 notes = ",int(One))
if FiftyP>0:
	print("50p coins = ",int(FiftyP))
if TwentyP>0:
	print("20p coins = ",int(TwentyP))
if TenP>0:
	print("10p coins = ",int(TenP))
if FiveP>0:
	print("5p coins = ",int(FiveP))
if TwoP>0:
	print("2p coins = ",int(TwoP))
if OneP>0:
	print("1p coins = ",int(OneP))