#list-->Ordered--default index
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list1,type(list2))
list3=[10,20.2,30+3j,True,"python"]
print(list1,type(list3))
list5=[101,202,303,405]
print(list1,type(list5))
list5.append(501)
print(list5,type(list5))
list5.extend([601,701])
print(list5,type(list5))
list5.insert([4,51])
print(list5,type(list5))
list5.pop()
print(list5,type(list5))
list5.pop(0)
print(list5,type(list5))
del list5[1]
print(list5,type(list5))