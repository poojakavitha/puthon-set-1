x=int(input())
i=1
while(i<=x):
    k=0
    if(x%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i,end=" ")
    i=i+1
