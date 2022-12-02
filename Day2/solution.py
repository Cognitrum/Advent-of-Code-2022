shape_scores = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

def round (opp_score, you_score):
    if (opp_score == you_score):
        return 3 + you_score
    if (opp_score == 1 and you_score == 2):
        return  6 + you_score
    if (opp_score == 2 and you_score == 3):
        return  6 + you_score
    if (opp_score == 3 and you_score == 1):
        return  6 + you_score
    if (opp_score == 1 and you_score == 3):
        return  0 + you_score
    if (opp_score == 3 and you_score == 2):
        return  0 + you_score
    if (opp_score == 2 and you_score == 1):
        return  0 + you_score

def det_round(opp_score, round_result):
    if (round_result == "Z"):
        if (opp_score == 1):
            return  6 + 2
        if (opp_score == 2):
            return  6 + 3
        if (opp_score == 3):
            return  6 + 1
    if (round_result == "Y"):
        if (opp_score == 1):
            return  3 + 1
        if (opp_score == 2):
            return  3 + 2
        if (opp_score == 3):
            return  3 + 3
    if (round_result == "X"):
        if (opp_score == 1):
            return  0 + 3
        if (opp_score == 2):
            return  0 + 1
        if (opp_score == 3):
            return  0 + 2



def tournament():
    file = open("C:\\Users\\Aaron\\Desktop\\Hold\\Advent-Of-Code-2022\\Day2\\input.txt", "r")
    part1_score = 0
    part2_score = 0

    for x in file:
        if (x != "\n"):
            temp = x.split(" ")
            part1_score += round(shape_scores[temp[0]],shape_scores[temp[1].replace("\n","")])
            part2_score += det_round(shape_scores[temp[0]],temp[1].replace("\n",""))

    print(f"Part 1 Score: {part1_score}")
    print(f"Part 2 Score: {part2_score}")

tournament()