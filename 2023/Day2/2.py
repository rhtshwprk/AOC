def main():
    inputList = []
    with open('2.txt') as fd:
        for line in fd:
            inputList.append(line)

    twoA(inputList)
    print()

def twoA(list):
    print(list)

if (__name__ == '__main__'):
    main()