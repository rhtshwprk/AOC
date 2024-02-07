import re

def main():
    winning = []
    nums = []
    with open('./inputs/4.txt') as fd:
        for line in fd:
            lineShort = (line[line.find(':')+2:])
            winning.append(lineShort[0:lineShort.find('|')])
            nums.append(lineShort[lineShort.find('|')+1:len(lineShort)-1])  

    for i,win in enumerate(winning):
        winStrArr=re.split('\s+',win.strip())
        winNumArr=[]
        for num in winStrArr:
            winNumArr.append(int(num))
        winning[i]=(winNumArr)

    for i,win in enumerate(nums):
        numsStrArr=re.split('\s+',win.strip())
        numsNumArr=[]
        for num in numsStrArr:
            numsNumArr.append(int(num))
        nums[i]=(numsNumArr)

    numCards = [1]*len(winning)
    # print(numCards)


    sumScore=0
    for i,(x,y) in enumerate(zip(winning,nums)):
        sumScore+=pointWorth(x,y)
        numCards=cardCount(x,y,numCards,i)
    print(sum(numCards))
    # print(sumScore)
    # print(winning)
    # print(nums)

def pointWorth(winning, nums):
    score = 0
    count = 0
    for num in nums:
        if(num in winning):
            score = 2**count
            count+=1
    return score

def cardCount(winning, nums, numCards, cardNum):
    count = 0
    for i,num in enumerate(nums):
        if(num in winning):
            count+=1
    for j in range(cardNum+1,cardNum+1+count):
        numCards[j]+=numCards[cardNum]
    # print(numCards)
    return numCards



if(__name__ == '__main__'):
    main()
