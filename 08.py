#list comprehension
result=[]
for i in range(11):
    result.append(i)
    print(result)

#list comprehension version
print([i for i in range(11)])

#for loop verison
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)

print([i for i in range(11)if i%2!=0])

result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else :
        result.append(i**2)
print(result)

print([i for i in range(11)if i%2!=0])

result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else :
        result.append(i**2)
print(result)

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]