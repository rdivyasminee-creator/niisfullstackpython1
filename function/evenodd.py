def check():
		print("enter a number")
		n=int(input())
		if n%2==0:
			return True
		else:
			return False
		n=int(input())
if check():
   print("even number")
else:
  	print("odd number")

   

print("enter a number")
n=int(input())
check(n)