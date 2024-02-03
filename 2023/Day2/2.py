sumID = 0

def main():
    inputList = []
    bagContains = [12,13,14]
    with open('2.txt') as fd:
        for line in fd:
            inputList.append(line)


    possibleGames = 0
    totalPower =0
    for i,str in enumerate(inputList):
        id = i+1
        power = calculatePower(str)
        totalPower+=power
        print(f"power= {totalPower}")
        # if(checkEntry(str,bagContains)):
        #     possibleGames+=id
    # print(possibleGames)
    print(f"Total Power= {totalPower}")

def checkEntry(str, bagContains):
    str_minus_number = str[str.find(':')+1:]
    split_arr = str_minus_number.split(';')
    # print(split_arr)
    for entry in split_arr:
        isPossible=True
        stripped_entry = entry.strip()
        number = ""
        num = 0
        for i,ch in enumerate(stripped_entry):
            if (ch.isdigit()):
                number+=ch
            else:
                if(ch==' '):
                    if(number):
                        num = int(number)
                        number = ""
                elif(ch=='r' and stripped_entry[i-1]==' '):
                    if(bagContains[0]<num):
                        print(f"entry: {stripped_entry}")
                        print(f"red: {num} vs Bagcontains red:{bagContains[0]}")
                        return False
                elif(ch=='g' and stripped_entry[i-1]==' '):
                    if(bagContains[1]<num):
                        print(f"entry: {stripped_entry}")
                        print(f"green: {num} vs Bagcontains green:{bagContains[1]}")
                        return False
                elif(ch=='b' and stripped_entry[i-1]==' '):
                    if(bagContains[2]<num):
                        print(f"entry: {stripped_entry}")
                        print(f"blue: {num} vs Bagcontains blue:{bagContains[2]}")
                        return False
        
    return True

def calculatePower(str):
    str_minus_number = str[str.find(':')+1:]
    split_arr = str_minus_number.split(';')
    minR=minG=minB=-1
    print(split_arr)
    for entry in split_arr:
        isPossible=True
        stripped_entry = entry.strip()
        number = ""
        num = 0
        for i,ch in enumerate(stripped_entry):
            if (ch.isdigit()):
                number+=ch
            else:
                if(ch==' '):
                    if(number):
                        num = int(number)
                        number = ""
                elif(ch=='r' and stripped_entry[i-1]==' '):
                    if(minR==-1 or minR<num):
                        # print(f"min red changed from {minR} to {num}")
                        minR = num
                elif(ch=='g' and stripped_entry[i-1]==' '):
                    if(minG==-1 or minG<num):
                        # print(f"min green changed from {minG} to {num}")
                        minG = num

                elif(ch=='b' and stripped_entry[i-1]==' '):
                    if(minB==-1 or minB<num):
                        # print(f"min blue changed from {minB} to {num}")
                        minB = num
    if(minG==-1 or minB==-1 or minR==-1):
        return 0
    print(f"returning {minR}*{minG}*{minB} = {minB*minG*minR}")
    return (minG*minB*minR)  


if (__name__ == '__main__'):
    main()