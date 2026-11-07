category_2_patterns = {}

def get_top_winrate_games(num, minimum_games):

    sorted_patterns = []

    for pattern, values in category_1_patterns.items():

        frequency, wins, draws, losses = values

        if frequency < minimum_games:
            continue

        win_rate = wins / frequency

        sorted_patterns.append(pattern, win_rate, frequency)

    sorted_patterns.sort(key=lambda x: x[1], reverse=True)

    return sorted_patterns[:num]

def find_category_2_pattern(size, result, moves, top_patterns):

    added_patterns = set() # unique patterns should only be counted once
    number_of_moves = len(moves)
    
    if size > number_of_moves:
        return

    top_keys = {item[0] for item in top_keys}

    cat_1_pattern = {}

    for i in range(size):
            cat_1_pattern[moves[i][0]] = cat_1_pattern.get(moves[i][0], 0) + 1

    for l in range(number_of_moves - size + 1):

        cat_1_pattern_key = tuple(sorted(cat_1_pattern.items()))

        if cat_1_pattern_key in top_keys:

            ordered_pattern_key = tuple(move[0] for move in moves[l:l+size])

            if ordered_pattern_key not in added_patterns:

                added_patterns.add(ordered_pattern_key)

                # checks if pattern is in dictionary and gets 0 tuple or the values for that ordered pattern
                values = category_2_patterns.get(ordered_pattern_key,(0,0,0,0))
                # updates pattern count in dictionary
                if result == 1:
                    category_2_patterns[ordered_pattern_key] = (values[0] + 1, values[1] + 1, values[2], values[3])
                elif result == 0:
                    category_2_patterns[ordered_pattern_key] = (values[0] + 1, values[1], values[2] + 1, values[3])
                elif result == -1:
                    category_2_patterns[ordered_pattern_key] = (values[0] + 1, values[1], values[2], values[3] + 1)

                

        # move pointer
        if l < number_of_moves - size:
        
            # get rid of old move
            old_move = moves[l][0]
            cat_1_pattern[old_move] -= 1
        
            if cat_1_pattern[old_move] == 0:
                del cat_1_pattern[old_move]

            # add the new move
            new_piece = moves[l + size][0]
            cat_1_pattern[new_piece] = cat_1_pattern.get(new_piece, 0) + 1
    

