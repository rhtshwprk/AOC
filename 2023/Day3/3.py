def main():
    input = []
    
    with open('./3.txt') as fd:
        for line in fd:
            input.append(list(line[0:(len(line)-1 if line[len(line)-1]=='\n' else len(line))]))  #removes newline escapes from the lists except for last line

    #this code type converts digits (character => integer)      
    for i,line in enumerate(input):
        for j,x in enumerate(line):
            if(x.isdigit()):
                input[i][j] = int(x)
            else:
                input[i][j] = x

    #this code converts all digits to the number they constitute
    for i,line in enumerate(input):
        l = len(line)
        num = 0
        numberIndices=[]
        for j,x in enumerate(line):
            if(isinstance(x,int)):
                num = num*10+x
                numberIndices.append(j)
                if(j==l-1 or line[j+1]=='.' or not isinstance(line[j+1], int)):   
                    for index in numberIndices:
                        input[i][index]=num
                    num=0
                    numberIndices = []
    #[467, 467, 467, '.', '.', 114, 114, 114, '.', '.']
    #['.', '.', '.', '*', '.', '.', '.', '.', '.', '.']
    #['.', '.',  35, 35,  '.', '.', 633, 633, 633, '.']
    #['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
    #[617, 617, 617, '*', '.', '.', '.', '.', '.', '.']
    #['.', '.', '.', '.', '.', '+', '.',  58,  58, '.']
    #['.', '.', 592, 592, 592, '.', '.', '.', '.', '.']
    #['.', '.', '.', '.', '.', '.', 755, 755, 755, '.']
    #['.', '.', '.', '$', '.', '*', '.', '.', '.', '.']
    #['.', 664, 664, 664, '.', 598, 598, 598, '.', '.']
                    
    for line in input:
        print(line)                 

    # print(f"output: {sum_calculator(input)}")
    print(f"sum of gear ratios: {gearRatioCalculator(input)}")

def printSymbols(input):
    symbols={}
    symStr= ""
    for line in input:
        for x in line:
            if(not isinstance(x,int) or not x.isdigit() and not x=='.'):
                symbols[x]=1
    
    for value in symbols:
        symStr+=value
    return symStr
#returned:  *%@#+$-=/&

def checkNeighbours(input,i,j):
    symbols = (printSymbols(input))
    try:
        if(input[i][j+1] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i][j-1] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i-1][j-1] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i-1][j] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i-1][j+1] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i+1][j-1] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i+1][j] in symbols):
            return True
    except:
        print('no')
    try:
        if(input[i+1][j+1] in symbols):
            return True
    except:
        print('no')
    return False

def sum_calculator(input):
    sum= 0
    symbols = printSymbols(input)
    adjacent = False
    for i,line in enumerate(input):
        # print(line)
        num = 0
        num_string = ""
        for j,x in enumerate(line):
            l = len(line)
            if(x.isdigit()):
                if(checkNeighbours(input,i,j)):
                    # print(f"input[{i}][{j}]={x}, adjacent:{True}")
                    adjacent = True
                num_string+=x
                if(j==l-1 or line[j+1]=='.' or line[j+1] in symbols):   
                    num = int(num_string)
                    # print(f"{num}, adjacent:{adjacent}")
                    if (adjacent):
                        sum+=num
                    num_string=""
                    num=0
                    adjacent=False
        ## todo: Check for adjacency
        ##
    return sum

def gearRatioCalculator(input):
    sum = 0
    for i, line in enumerate(input):
        for j, x in enumerate(line):
            if(x == '*'):
                adjacentNums = []
                for i1 in range(i-1,i+2):
                    adjacentNumsInLine = []
                    for j1 in range (j-1,j+2):
                        if(i1>=0 and i1<len(input) and j1>=0 and j1<=len(line)):
                            # print(f"check {i1}/{j1} for * {i}/{j}")
                            if (isinstance(input[i1][j1],int)):
                                if (not input[i1][j1] in adjacentNumsInLine):
                                    adjacentNumsInLine.append(input[i1][j1])
                    adjacentNums.extend(adjacentNumsInLine)
                print(adjacentNums)
                if(len(adjacentNums)==2):
                    sum+= adjacentNums[0]*adjacentNums[1]
    
    return sum
                            
            
if __name__ == '__main__':
    main()

