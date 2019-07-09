a,b=map(str,input().split())
if len(a)!=len(b):
  print("no")
else:
  d1=[a.count(i) for i in a]
  d2=[b.count(i) for i in b]
if d1==d2:
  print("Yes")
else:
  peint("no")
