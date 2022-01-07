a=int(input())
r=0
def solution(a):
    for i in range(1,a+1):

        b=list(map(int,str(i)))
        c=i+sum(b)
        if c==a:
            r=i
            break
    return print(r)

solution(a)




