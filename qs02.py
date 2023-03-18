c=("Choose which currency you have")
c1=("1.euro")
c2=("2.rs")
c3=("3.rv")
c4=("4.cd")
choose=int(input("1/2/3/4"))
urc=int(input("input urc"))
if choose==1:
    print(0.01417)
elif choose==2:
    print(0.0100*urc)
elif choose==3:
    print(0.02140*urc)
elif choose==4:
    print(0.02027*urc)