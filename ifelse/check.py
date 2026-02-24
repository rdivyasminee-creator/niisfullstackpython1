print("enter a number")
no=int(input())
if no<=9:
	print("single digit")
elif no<=99:
	print("double digit")
elif no<=999:
     print("triple digit")
elif no>0:
	print("+ve")
else:
	print("other digit")
