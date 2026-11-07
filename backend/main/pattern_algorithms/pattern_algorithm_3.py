category_3_patterns = {}
def find_category_3_patterns(size,moves,result,cat_2_patterns):
    added_pattern_and_actions = set() # unique patterns and actions should only be counted once
    number_of_moves = len(moves)

    if size > number_of_moves:
        return

    for l in range(number_of_moves - size + 1):

        ordered_pattern_key = tuple(move[0] for move in moves[l:l+size])

        if ordered_pattern_key not in cat_2_patterns:
            continue

        pattern_and_action_key = tuple(moves[l:l+size])

        if pattern_and_action_key in added_pattern_and_actions:
            continue

        added_pattern_and_actions.add(pattern_and_action_key) # add pattern and action to hashset

        # checks if pattern is in dictionary and gets 0 tuple or the values for that pattern and action 
        values = category_3_patterns.get(pattern_and_action_key,(0,0,0,0))
        # updates pattern count in dictionary
        if result == 1:
            category_3_patterns[pattern_and_action_key] = (values[0] + 1, values[1] + 1, values[2], values[3])
        elif result == 0:
            category_3_patterns[pattern_and_action_key] = (values[0] + 1, values[1], values[2] + 1, values[3])
        elif result == -1:
            category_3_patterns[pattern_and_action_key] = (values[0] + 1, values[1], values[2], values[3] + 1)

