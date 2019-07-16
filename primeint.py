av,bd=map(int,input().split())
for i in range(av+1,bd):
  for z in range(2,i):
    if(i%z==0):
      break
  else:
      print(i,end=" ")
