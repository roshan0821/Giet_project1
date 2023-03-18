bnum=[]
n=5
i=0
while n!=0:

    rem=n%2
    bnum.insert(i,rem)
    i=i+1
    n=n//2

i=i-1
while i>=0:
    print(end=str(bnum[i]))
    i=i-1
