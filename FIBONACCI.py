n = int(input("Enter a Number: "))
fibo=[]
c,n1,n2=0,0,1
if n==1:print(n1)
else:
	while(c<n):
		fibo.append(n1)
		t=n1+n2
		n1,n2 = n2,t
		c+=1
print(fibo)
