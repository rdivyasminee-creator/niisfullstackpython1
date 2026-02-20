num = int(input("enter a number:"))
last_digit = num% 10
if last_digit %2==0:
	print("the last digit is even")
else:
	print("the last digit is odd")