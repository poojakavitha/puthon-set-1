def printRepeating(arr,size) : 
    count = [0] * size 
    print(" Repeating elements are ",end = "") 
    for i in range(0, size) : 
        if(count[arr[i]] == 1) : 
            print(arr[i], end = " ") 
        else : 
            count[arr[i]] = count[arr[i]] + 1
t=int(input())
arr=[]
for i in range(0,t):
  print(arr[i])
printrepeating(arr,len(arr))
