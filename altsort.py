nn=int(input())
lis=list(map(int,input().split()))
c=sorted(lis)
d=c[::-1]
e=[]
for i in range(0,len(lis)):
  e.append(d[i])
  e.append(c[i])
for j in e[:len(lis)]:
  print(j,end=" ")
