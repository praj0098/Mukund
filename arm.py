ak80=int(input())
sum=0
n=ak80
while n>0:
  digit=n%10
  sum+=digit**3
  n//=10
if ak80==sum:
  print("yes")
else:
  print("no")
