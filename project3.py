n=int(input("Enter number of elements: "))
list1=[]
result=[]
for i in range(0,n):
    list1.append(int(input()))
for i in list1:
    if i>=0:
        result.append(i)
print(result)
