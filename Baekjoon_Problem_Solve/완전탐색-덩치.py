a=int(input())

b=[]
for _ in range(a):
    w,h=map(int,input().split())
    b.append((w,h))

for i in range(len(b)):
    count=1
    for j in range(len(b)):
        if b[i][0]<b[j][0] and b[i][1]<b[j][1]:
            count+=1
    print(count,end=' ')