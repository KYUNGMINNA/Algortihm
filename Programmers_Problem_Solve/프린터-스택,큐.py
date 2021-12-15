def solution(priorities, location):
    answer = 0
    while priorities:
        maxs=max(priorities)
        popnum=priorities.pop(0)
        if maxs==popnum:
            answer+=1
            if location==0:
                break
            else:
                location -=1
        else:
            priorities.append(popnum)
            if location==0:
                location=len(priorities)-1
            else:
                location-=1
    return answer
priorities=[2,1,3,2]
location=2
solution(priorities,location)

