a=input()
b=['a','e','i','o','u','A','E','I','O','U']
c=[]
for i in a:
  if i not in b:
    c.append(i)
print(''.join(c[::-1]))
