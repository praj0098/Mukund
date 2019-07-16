aa,bb=list(map(int,input().split()))
cc=list(map(int,input().split()))
dd=[]
for i in cc:
    if i<=i+1:
        dd.append(i)
print(dd[bb-1])
