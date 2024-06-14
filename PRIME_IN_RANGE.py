# Input from Console
l,u = map(int,input("Enter Lower and Upper Limits: ").split())
Prime = list()
for num in range(l,u+1):
	if num>1:
		for i in range(2,num):
			if num%2==0:break
		else:Prime.append(num)
print(Prime)

'''
# Input from CMD Line Arguments
import sys
l,u = int(sys.argv[1]),int(sys.argv[2])
Prime = list()
for num in range(l,u+1):
	if num>1:
		for i in range(2,num):
			if num%2==0:break
		else:Prime.append(num)
print(Prime)
'''