import heapq

def get_top_winrate_games(num, minimum_games, category_patterns):

    sorted_patterns = [] # tuple(win_rate, pattern) win rate first to sort it by win rate

    for pattern, values in category_patterns.items():

        frequency, wins, draws, losses = values

        if frequency < minimum_games:
            continue

        win_rate = wins / frequency

        if len(sorted_patterns) < num:
            heapq.heappush(sorted_patterns,(win_rate,pattern))
        elif win_rate > sorted_patterns[0][0]:
            heapq.heapreplace(sorted_patterns,(win_rate,pattern))

    return [pattern for win_rate,pattern in sorted(sorted_patterns, reverse=True)]
