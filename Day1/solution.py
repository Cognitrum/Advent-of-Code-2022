f = open("C:\\Users\\Aaron\\Desktop\\Hold\\Advent-Of-Code-2022\\Day1\\input.txt", "r")
sum = 0
elves = []
for x in f:
    if (x != "\n"):
        sum += int(x)
    else:
        elves.append(sum)
        sum = 0

print(f"Max elf: {max(elves)}")

elves.sort(reverse=True)
sum = 0
for i in range(3):
    sum += elves[i]

print(f"Top 3 elves: {sum}") 