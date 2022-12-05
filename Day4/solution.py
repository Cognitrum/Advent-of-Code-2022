
file = open(".\\input.txt","r")

part1 = 0
part2 = 0

for x in file:
    temp = x.split(",")
    elf1 = temp[0].split("-")
    elf2 = temp[1].split("-")
    elf2[1] = elf2[1].replace("\n","")


    if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
        part1 += 1
    elif (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
        part1 += 1
    
    if ((int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])) or (int(elf1[1]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0]) )):
        part2 += 1
    elif ((int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1])) or (int(elf2[1]) <= int(elf1[1]) and int(elf2[1]) >= int(elf1[0]) )):
        part2 += 1

print(part1)
print(part2)