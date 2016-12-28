x = int(input())
temp = 0
while x != 0:
	digit = x % 10
	x /= 10
	temp = temp*10 + digit
print(temp)
