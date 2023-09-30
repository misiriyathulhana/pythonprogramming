n=int(input("how many numbers"))
sum=0
for i in range(n):
    x=int(input("enter the number:"))
    sum=sum+x
print("sum:",sum)
avg=sum/n
print("average=",avg)
