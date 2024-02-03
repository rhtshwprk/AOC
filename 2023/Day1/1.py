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

    for str in list:
        # print(str)
        i=0
        j=len(str)-1
        fIndex = -1
        rIndex = -1

        f= -1
        l= -1

        for alpha,num in alphaDigitMap.items():
            leftOcc = str.find(alpha)
            rightOcc = str.rfind(alpha)

            if(leftOcc !=-1):
                if(fIndex == -1 or fIndex>leftOcc):
                    fIndex = leftOcc
                    f = num
                    # print(f"left num: {f}, fIndex:{fIndex}")
                if(rIndex == -1 or rIndex<rightOcc):
                    rIndex = rightOcc
                    l= num
                    # print(f"right num: {l}, fIndex:{rIndex}")

        while(True):
            if(str[i].isdigit()):
                if(fIndex>i or fIndex ==-1):
                    f = int(str[i])
                    fIndex=i
            if(str[j].isdigit()):
                if(rIndex<j or rIndex ==-1):
                    l = int(str[j])
                    rIndex=j
            i+=1
            j-=1
            if (f!=-1 and l!=-1 and i>=fIndex and j<=rIndex):
                total+= 10*f + l
                print(f'{str} {(10*f+l)}')
                f=-1
                l=-1
                break
    return total


def main():
    list = []

    with open ('1.txt') as fd:
        for line in fd:
            list.append(line)
    
    # print(oneA(list))
    print(oneB(list))

if __name__ == '__main__':
    main()