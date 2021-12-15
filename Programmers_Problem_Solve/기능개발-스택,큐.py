def solution(progresses, speeds):
    a=[]
    num=0
    count=0
    while progresses:
        if progresses[0]+num*speeds[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if count>0:
                a.append(count)
                count=0
            num+=1
    a.append(count)
    return print(a)

progresses=[93,30,55]
speeds=[1,30,5]
solution(progresses,speeds)
# https://programmers.co.kr/learn/courses/30/lessons/42586