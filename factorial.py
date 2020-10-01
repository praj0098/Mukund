vijay = int(input())
factori = 1
for i in range(1,vijay+1):
  factori = factori*i
print(factori)

It can be done using recursiom

def fact(num):
  if num ==0 or num == 1:
    return 1
  else:
    return num*fact(num-1)
