a,d=input().split(' ')
b=int(d)
c=[]
for i in range(1,b+1):
    c.append(a[-i])
c.reverse()
print(''.join(c))
