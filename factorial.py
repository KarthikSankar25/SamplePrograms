x = int(input())
f = 1
if x == 0:
	print("1")
if x <= 0:
	print("Only non negative integer allowed")
if x >= 1:
	for i in range (1, x+1):
		f *= i
	print(f)
