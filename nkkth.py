aa,ba=map(int,input().split())
cc=input().split()
dd=[]
for i in cc:
    if (int(i)%2!=0):
        dd.append(i)
print(dd[ba-1])
