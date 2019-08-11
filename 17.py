l=int(input())
r=int(input())
if(l>r):
  min1=l
else:
  min1=r
while(1):
  if(min1%l==0 and min1%r==0):
    print(min)
    break
  min1=min1+1
