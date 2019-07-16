num=int(input())
sum=0
for i in range(2,num):
    if num%i==0:
        sum=sum+1
if sum>=1:
    print("no")
else:
    print("yes")
