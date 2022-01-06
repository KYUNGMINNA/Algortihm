
a,b=map(int,input().split())
c=list(map(int,input().split()))

from itertools import permutations

p=permutations(c,3)
answer=0
print(list(p))
for i in p:
    if b+1 >sum(i):
        answer=max(answer,sum(i))
print(answer)



for i in range(len(c)):
    for j in range(i+1,len(c)):
        for k in range(j+1,len(c)):
            su=c[i]+c[j]+c[k]
            if su<=b:
                answer=max(answer,su)
print(answer)

