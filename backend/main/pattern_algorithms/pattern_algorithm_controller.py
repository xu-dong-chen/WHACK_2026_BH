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
    training_games = len(games) * 80 // 100

    return games[:training_games], games[training_games:]

def get_real_patterns():
    games = getGames()
    training_games, validation_games = split_games(games)

    for game in training_games:
        find_category_1_patterns(8, game[2], game[0])
    for game in training_games:
        find_category_2_patterns(8, game[2], game[0], get_top_winrate_games(5, len(training_games) * 2 // 100, category_1_patterns, False))
    for game in training_games:
        find_category_3_patterns(8, game[2], game[0], get_top_winrate_games(5, len(training_games) * 5 // 1000, category_2_patterns, False))

    top_patterns = get_top_winrate_games(5, len(training_games) * 5 // 10000, category_3_patterns, False)

    for game in validation_games:
        find_top_patterns(8, game[2], game[0], top_patterns)

    results = []

    for pattern, values in list(new_patterns_and_actions.items()):
        training_frequency, training_wins, _, _ = category_3_patterns[pattern]
        validation_frequency, validation_wins, _, _ = values

        training_win_rate = training_wins / training_frequency
        validation_win_rate = validation_wins / validation_frequency

        if validation_win_rate > 0.5 and abs(validation_win_rate - training_win_rate) <= 0.1:
            results.append([pattern, validation_win_rate])

    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    
    return sorted_results