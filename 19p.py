n1,n2=map(int,input().split())
n3=0
for i in range(n1,n2+1):
  if j>1:
    for j in range(2,i):
      if i%j==0:
        break
      else:
        n3++
print(n3)
