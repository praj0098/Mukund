x,y,z=input().split()
if(x>=y) and (x>=z):
  large=x
elif(y>=x) and (y>=z):
  large=y
else:
  large=z
print(large)
