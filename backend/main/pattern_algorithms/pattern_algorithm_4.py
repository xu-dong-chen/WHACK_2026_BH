new_patterns_and_actions = {}
def find_top_patterns(size, result, moves, top_patterns):
    added_pattern_and_actions = set() # unique patterns and actions should only be counted once
    number_of_moves = len(moves)

    if size > number_of_moves:
        return

    for l in range(number_of_moves - size + 1):

        pattern_and_action_key = tuple(moves[l:l+size])

        if l == 0:
            print("Validation sequence:", pattern_and_action_key)
            print("Training patterns:", top_patterns)
            print("Match:", pattern_and_action_key in top_patterns)
        if pattern_and_action_key not in top_patterns:
            continue

        if pattern_and_action_key in added_pattern_and_actions:
            continue

        added_pattern_and_actions.add(pattern_and_action_key) # add pattern and action to hashset

        # checks if pattern is in dictionary and gets 0 tuple or the values for that pattern and action
        values = new_patterns_and_actions.get(pattern_and_action_key,(0,0,0,0))
        # updates pattern count in dictionary
        if result == 1:
            new_patterns_and_actions[pattern_and_action_key] = (values[0] + 1, values[1] + 1, values[2], values[3])
        elif result == 0:
            new_patterns_and_actions[pattern_and_action_key] = (values[0] + 1, values[1], values[2] + 1, values[3])
        elif result == -1:
            new_patterns_and_actions[pattern_and_action_key] = (values[0] + 1, values[1], values[2], values[3] + 1)