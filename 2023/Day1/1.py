def oneA(list):
    total = 0

    f= -1
    l= -1
    for str in list:
        i = 0
        j = len(str)-1
        while(True):
            if(str[i].isdigit()):
                f = int(str[i]) if f==-1 else f
            if(str[j].isdigit()):
                l = int(str[j]) if l==-1 else l
            i+=1
            j-=1
            if (f!=-1 and l!=-1):
                total+= 10*f + l
                # print(f'{str} {(10*f+l)}')
                f=-1
                l=-1
                break
    return total

def oneB(list):

    alphaDigitMap = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    # TODO
    # Check for letters and then run

    total = 0

    f= -1
    l= -1
    leftNum=''
    rightNum=''
    for str in list:
        i = 0
        j = len(str)-1
        while(True):
            if(str[i].isdigit()):
                f = int(str[i]) if f==-1 else f
            if(str[j].isdigit()):
                l = int(str[j]) if l==-1 else l
            
            leftNum+=str[i]
            rightNum = str[j]+rightNum

            i+=1
            j-=1
            if (f!=-1 and l!=-1):
                total+= 10*f + l
                # print(f'{str} {(10*f+l)}')
                f=-1
                l=-1
                break
    return total


def main():
    list = []

    with open ('2023/Day1/1.txt') as fd:
        for line in fd:
            list.append(line)
    
    print(oneA(list))
    print(oneB(list))

if __name__ == '__main__':
    main()