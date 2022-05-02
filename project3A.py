a=1
b=0
n=int(input("Enter a number "))
for i in range(n):
	if i==0:
		print(a,end=" ")
	elif i==1:
		print(b,end=" ")
	else:
		b=a+b
		a=b-a
		print(b,end=" ")
