from ..parser import getGames
from .get_top_win_rates import get_top_winrate_games
from .pattern_algorithm_2 import find_category_2_patterns
from .pattern_algorithm_2 import category_2_patterns
from .pattern_algorithm_3 import find_category_3_patterns
from .pattern_algorithm_3 import category_3_patterns

# category 1 in form (P, R, N, B, Q, K, O, =)
category_1_patterns = {}

# finds category 1 patterns of certain size
def find_category_1_pattern(size, result, moves):

    added_patterns = set() # unique patterns should only be counted once
    number_of_moves = len(moves)

    if size > number_of_moves:
        return

    pattern = {}
    for i in range(size):
        pattern[moves[i][0]] = pattern.get(moves[i][0], 0) + 1

    for l in range(number_of_moves - size + 1):

        pattern_key = tuple(sorted(pattern.items()))

        # checks if pattern has already been seen
        if pattern_key not in added_patterns:

            added_patterns.add(pattern_key) # add pattern to hashset

            # checks if pattern is in dictionary and gets 0 tuple or the values for that pattern 
            values = category_1_patterns.get(pattern_key,(0,0,0,0))

            # updates pattern count in dictionary
            if result == 1:
                category_1_patterns[pattern_key] = (values[0] + 1, values[1] + 1, values[2], values[3])
            elif result == 0:
                category_1_patterns[pattern_key] = (values[0] + 1, values[1], values[2] + 1, values[3])
            elif result == -1:
                category_1_patterns[pattern_key] = (values[0] + 1, values[1], values[2], values[3] + 1)


        # move pointer
        if l < number_of_moves - size:

            # get rid of old move
            old_move = moves[l][0]
            pattern[old_move] -= 1

            if pattern[old_move] == 0:
                del pattern[old_move]

            # add the new move
            new_piece = moves[l + size][0]
            pattern[new_piece] = pattern.get(new_piece, 0) + 1

games = getGames()
for game in games:
    find_category_1_pattern(5,game[2],game[0])
print(category_1_patterns)
print(get_top_winrate_games(5,3,category_1_patterns))

for game in games:
    find_category_2_patterns(5,game[2],game[0],get_top_winrate_games(5,3,category_1_patterns))
print(category_2_patterns)
print("\npattern 2 : ")
print(get_top_winrate_games(5,0,category_2_patterns))

for game in games:
    find_category_3_patterns(5,game[2],game[0],get_top_winrate_games(5,0,category_2_patterns))
print(category_3_patterns)
print("\npattern 3 : ")
print(get_top_winrate_games(5,0,category_3_patterns))
