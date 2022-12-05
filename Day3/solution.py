def part1() :
    file = open(".\\input.txt","r")

    chars = []
    sum = 0

    for x in file:
        temp = x.replace("\n","")
        sack1 = temp[:int((len(temp)/2))]
        sack2 = temp[int(len(temp)/2):]

        for i in sack1:
            if (i in sack2):
                chars.append(i)
                break
                


    for char in chars:
        if (char.isupper() ):
            sum += ord(char)-64 +26
        else:
            sum += ord(char)-96

    print(sum)

def part2():
    file = open(".\\input.txt","r")

    elf1, elf2, elf3 = "","",""
    counter = 0
    sum=0
    chars = []

    for x in file:
        if (counter == 0):
            elf1 = x.replace("\n", "")
            counter += 1
            continue
        if (counter == 1):
            elf2 = x.replace("\n", "")
            counter += 1
            continue
        if (counter == 2):
            elf3 = x.replace("\n", "")
            counter = 0

        for i in elf1:
            if((i in elf2) and (i in elf3)):
                chars.append(i)
                break
                print(elf1)
                print(elf2)
                print(elf3)
                print(i)

    for char in chars:
        if (char.isupper() ):
            sum += ord(char)-64 +26
        else:
            sum += ord(char)-96
    
    print(sum)


part2()
