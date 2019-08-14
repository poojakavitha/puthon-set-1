arr=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
size=len(arr)
arr.sort(reverse=True)
num=arr[0]
for i in range(1,size):
    num=num*10+arr[i]
print(num,end=" ")
