import chess.pgn

def getGames():
    pgn = open("../dataset/temp.pgn") # opens the dataset file NEED TO CHANGE TEMP.PGN
    games = [] # stores all the games and results each element is a tuple (moves,result)
    game = chess.pgn.read_game(pgn)
    while game is not None: # loops through all the games
        moves = [] # moves for that game

        for move in game.mainline():
            move = move.san()

            # check if move is castle
            if move == "O-O":
                moves.append("O2")
                continue
            if move == "O-O-O":
                moves.append("O3")
                continue

            move_cleaned = ""

            # check for pawn moved/capture
            if move[0].islower():
                move_cleaned += "P"
            else:
                move_cleaned += move[0]

            # check for capture or move
            if "x" in move:
                move_cleaned += "x"
            else:
                move_cleaned += "m"
            #print(move_cleaned)
            moves.append(move_cleaned)

        # checks for who won 1 - white 0 - draw -1 - black
        winner = 0
        res = game.headers["Result"]
        if res == "1-0":
            winner = 1
        elif res == "0-1":
            winner = -1
        else:
            winner = 0

        games.append((moves,winner))

        game = chess.pgn.read_game(pgn)
    #print(games)
    return games

print(getGames())