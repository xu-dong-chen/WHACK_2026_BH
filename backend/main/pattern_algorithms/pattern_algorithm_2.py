def find_category_2_pattern(size, result, moves, top_patterns):

    added_patterns = set() # unique patterns should only be counted once
    number_of_moves = len(moves)
    
    if size > number_of_moves:
        return

    pattern = []
    for i in range(size):
        pattern.append(moves[i][0])

    for j in range(number_of_moves - size + 1):
        
        patern_key = tuple(pattern)

        category_1_key = tuple
