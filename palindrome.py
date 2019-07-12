y=int(input())
a=y
s=0
while y!=0:
  d=y%10
  s=s*10+d
  y=y//10
if(s==a):
  print('yes')
else:
  print('no')
