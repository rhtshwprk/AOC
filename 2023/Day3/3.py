def main():
    input = []
    with open('./example.txt') as fd:
        for line in fd:
            input.append(list(line[0:(len(line)-1 if line[len(line)-1]=='\n' else len(line))]))  #removes newline escapes from the lists except for last line
            
    # print(input)
    print(f"output: {sum_calculator(input)}")

def sum_calculator(input):
    sum= 0
    adjacent = True
    for i,line in enumerate(input):
        print(line)
        num = 0
        num_string = ""
        for j,x in enumerate(line):
            l = len(line)
            if(x.isdigit()):
                num_string+=x
                if(j==l-1 or line[j+1]=='.'):
                    num = int(num_string)
                    num_string=""
                    if (adjacent):
                        sum+=num
                    num=0
        ## todo: Check for adjacency
        ##
    return 1

if __name__ == '__main__':
    main()

