
number=int(input())

def Tower_of_Hanoi(number,a1,a2,a3):
    if number==1:
        print(a1,a3)
    else:
        Tower_of_Hanoi(number-1,a1,a3,a2)
        print(a1,a3)
        Tower_of_Hanoi(number-1,a2,a1,a3)


print(2**number-1)


Tower_of_Hanoi(number,1,2,3)

