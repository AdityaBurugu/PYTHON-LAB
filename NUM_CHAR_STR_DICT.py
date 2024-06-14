'''
#Case I:
name=input('Enter a String Name')

counts={}

for char in name:
        counts[char]=counts.get(char,0)+1
print(counts)
'''
'''
#Case II:
name=input('Enter a String Name')

counts={}

for char in name:
        counts[char] = name.count(char)
print(counts)
'''
'''
#Case III:
name=input('Enter a String Name')
counts={}
for x in name:
	if x not in counts:
		counts[x]=1
	else:
		counts[x]= counts[x]+1

print(counts)
'''
'''
#Case IV:
name=input('Enter a String Name')
counts={}
for x in name:
    keys=counts.keys()
    print(keys)
    if x in keys:
        counts[x]=counts[x]+1
    else:
        counts[x]= 1

print(counts)
'''

#Case V:
name=input('Enter a String Name')
counts={}
for x in name:
    if x in counts:
        counts[x]=counts[x]+1
    else:
        counts[x]= 1

print(counts)
