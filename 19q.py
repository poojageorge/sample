num=input("enter a num:")
n1,n2=0,1
count=0
if num<=0:
    print("enter pos integer")
elif num==0:
    print("fibonocci seq upto",num)
    print(n1)
else:
    print("fibonocci seq")
    while(count<num):
    n=n1 + n2
    n1 = n2
    n2 = n
    count += 1