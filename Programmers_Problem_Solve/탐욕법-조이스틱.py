def solution(name):
    change=[min(ord(i)-ord('A'),ord('Z')-ord(i)+1) for i in name]
    index=0
    answer=0


    while 1:
        answer+=change[index]
        change[index]=0
        if sum(change)==0:
            return print(answer)
        left,right=1,1
        while change[index-left]==0:
            left+=1
        while change[index+right]==0:
            right+=1
        answer+=left if left<right else right
        index+=-left if left<right else right

solution("JAZ")