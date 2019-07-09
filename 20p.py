a,b=list(map(str,input().split(" ")))
c=len(a)
d1=0
for i in range(c):
  if(a[i]!=b[i]):
    d1+=1
if d1==1:
  print("Yes")
else:
  print("no")
