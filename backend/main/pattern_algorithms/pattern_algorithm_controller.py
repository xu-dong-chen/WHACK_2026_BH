from ..parser import getGames
from .get_top_win_rates import get_top_winrate_games
from .pattern_algorithm_1 import find_category_1_patterns
from .pattern_algorithm_1 import category_1_patterns
from .pattern_algorithm_2 import find_category_2_patterns
from .pattern_algorithm_2 import category_2_patterns
from .pattern_algorithm_3 import find_category_3_patterns
from .pattern_algorithm_3 import category_3_patterns
from .pattern_algorithm_4 import find_top_patterns
from .pattern_algorithm_4 import new_patterns_and_actions

def split_games(games):
    training_games = len(games) * 60 // 100
    validation_games = len(games) * 80 // 100

    return games[:training_games], games[training_games:validation_games], games[validation_games:]


games = getGames()
training_games, validation_games, test_games = split_games(games)

for game in training_games:
    find_category_1_patterns(20, game[2], game[0])
for game in training_games:
    find_category_2_patterns(20, game[2], game[0], get_top_winrate_games(5, len(training_games) * 2 // 100, category_1_patterns, False))
for game in training_games:
    find_category_3_patterns(20, game[2], game[0], get_top_winrate_games(5, len(training_games) * 5 // 1000, category_2_patterns, False))

for game in validation_games:
    find_top_patterns(20, game[2], game[0], get_top_winrate_games(20, len(training_games) * 5 // 10000, category_3_patterns, False))
