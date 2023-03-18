#categories of functions based on arguments
#1.Positional argument
def function(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function(10,20,30,40)
#function(12,34)
function(23,"rs",23,35)

#Keyword arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(num1=10,num2=34,num4=23,num3=224)

#default arguments
def function2(name,rollno,branch="ECE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function2("Roshan",4)
#function2("Rupa",3,)

#variable number of arguments
def function3(*var):
    for i in var:
        print(i, end=" ")
function3(10,20)
print()  
function3(10,34,52,24,52)
print()  
function3(10,20,45,34,67,98,56,52)
print()  

#2
def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return(sum)
print