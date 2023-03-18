#even-->cube it
data=[1,2,3,4,5,6,7]
result=[i*i*i for i in data if i%2==0]
print(result)

#for loop--odd -->square it
data=[1,2,3,4,5,6,7]
result=[i*i for i in data if i%2!=0]
print(result) 