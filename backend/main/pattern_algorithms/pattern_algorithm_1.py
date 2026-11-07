# first move is White's

# category 1 in form (P, R, N, B, Q, K, O, =)
category_1_patterns = {}

result = 0
arrayVar = []

# finds category 1 patterns of certain size
def find_category_1_pattern(size):

    added_patterns = []

    for i in range(len(arrayVar) - size + 1):

        for j in range(size):

            pCount = 0
            rCount = 0
            nCount = 0
            bCount = 0
            qCount = 0
            kCount = 0
            oCount = 0
            equalsCount = 0

            if arrayVar[i + j][0] == "P":
                pCount += 1
            elif arrayVar[i + j][0] == "R":
                rCount += 1
            elif arrayVar[i + j][0] == "N":
                nCount += 1
            elif arrayVar[i + j][0] == "B":
                bCount += 1
            elif arrayVar[i + j][0] == "Q":
                qCount += 1
            elif arrayVar[i + j][0] == "K":
                kCount += 1
            elif arrayVar[i + j][0] == "Q":
                qCount += 1
            elif arrayVar[i + j][0] == "O":
                oCount += 1
            elif arrayVar[i + j][0] == "=":
                equalsCount += 1
            else:
                print("Error! 1")
    
        pattern = (pCount, rCount, nCount, bCount, qCount, kCount, qCount, oCount, equalsCount)

        # checks if pattern has already been iterated in index
        if pattern in added_patterns:
            continue

        # checks if pattern is in dictionary
        if pattern not in category_1_patterns:
            category_1_patterns[pattern] = (0, 0, 0, 0)

        patternCount, wins, draws, losses = category_1_patterns[pattern]

        # updates pattern count in dictionary
        if result == 1:
            category_1_patterns = (patternCount + 1, wins + 1, draws, losses)
        elif result == 0:
            category_1_patterns = (patternCount + 1, wins, draws + 1, losses)
        elif result == -1:
            category_1_patterns = (patternCount + 1, wins, draws, losses + 1)

        added_patterns.append(pattern)

