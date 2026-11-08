import chess.pgn
from pathlib import Path

def getGames():
    pgn_path = Path(__file__).resolve().parent.parent / "dataset" / "dataset.pgn" # opens the dataset file NEED TO CHANGE TEMP.PGN
    with open(pgn_path, encoding="utf-8") as pgn:
    
        games = [] # stores all the games and results each element is a tuple (moves,result)
        game = chess.pgn.read_game(pgn)
        while game is not None: # loops through all the games
            # moves for that game
            white = []
            black = []
            white_move = True
            for move in game.mainline():
                move_cleaned = ""
                move = move.san()

                # check if move is castle
                if move == "O-O":
                    move_cleaned = "O2"
                    continue
                if move == "O-O-O":
                    move_cleaned = "O3"
                    continue
                if "=" in move:
                    move_cleaned = "=p"
                    continue

                if move_cleaned == "":

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
                if white_move:
                    white.append(move_cleaned)
                else:
                    black.append(move_cleaned)
                white_move = not white_move
                #print(move_cleaned)

            # checks for who won 1 - white 0 - draw -1 - black
            winner = 0
            res = game.headers["Result"]
            if res == "1-0":
                winner = 1
            elif res == "0-1":
                winner = -1
            else:
                winner = 0

            games.append((white,black,winner))

            game = chess.pgn.read_game(pgn)
        #print(games)
        return games

#print(getGames())