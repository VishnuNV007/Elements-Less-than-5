

#Method1

a=[1,1,2,3,5,8,13,21,34,55,89]
for i in a:
	if i<5:
		print(i, end=" ")
print()

#Method2
a=[1,1,2,3,5,8,13,21,34,55,89]
lst=[]
for i in a:
	if i<5:
		lst.append(i)
print(lst)