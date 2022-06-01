n=int(input())
x=list(map(int,input().split()))
m=[]
c=[]
for i in x:
    if i%2==1:
        m.append(i)
    if i%2!=1:
        c.append(i)
print(*(m+c))