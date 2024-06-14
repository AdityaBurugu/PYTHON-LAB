'''
#Case I:
from statistics import *
l=[15,18,2,36,12,78,5,6,6,9,79]
print("Mean:",mean(l))
print("Median:",median(l))
print("Mode:",mode(l))

Case II:
'''
list_a=[99,22,9944,22,33,44]
n=len(list_a)
get_sum=0
for x in list_a:
	get_sum=get_sum+x
mean=get_sum/n
print("Mean of Elements in The List is:",mean)

list_a.sort()
if n%2==0:
	m1=list_a[n//2]
	m2=list_a[n//2-1]
	median=(m1+m2)/2
else:
	median=list_a[n//2]

print("Median is:",median)

num_list=list_a
counts=dict()

for x in num_list:
	if x not in counts:
		counts[x]=1
	else:
		counts[x]= counts[x]+1

max_value=max(list(counts.values()))

mode_value=list()

for k,v in counts.items():
	if v==max_value:
		mode_value.append(k)

n=len(num_list)

if len(mode_value)==n:
	print("NO MODE")
else:
	print("The List of Modes:",mode_value)
