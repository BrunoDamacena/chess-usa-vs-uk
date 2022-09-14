import chess
import chess.pgn
import chess.engine
from datetime import datetime


engine_path = '../../Stockfish/src/stockfish'
white_usa_fen = 'rnb1kbnr/pppppppp/8/8/8/8/PPPPPPPP/1NBQKBN1 w kq - 0 1'
black_usa_fen = '1nbqkbn1/pppppppp/8/8/8/8/PPPPPPPP/RNB1KBNR w KQ - 0 1'

usa = 'USA (No Rooks)'
uk = 'UK (No Queen)'


async def play_game(usa_color, time_limit, num):
    print(f'Playing game {num}. USA is {usa_color}')
    _, engine = await chess.engine.popen_uci(engine_path)
    if usa_color == 'white':
        event = 'USA is white, UK is Black'
        white = usa
        black = uk
        fen = white_usa_fen
    elif usa_color == 'black':
        event = 'USA is black, UK is White'
        white = uk
        black = usa
        fen = black_usa_fen
    else:
        return 0
    game = chess.pgn.Game()
    game.headers['Event'] = event
    game.headers['Site'] = 'https://github.com/BrunoDamacena/chess-usa-vs-uk'
    game.headers['Date'] = datetime.now().strftime('%Y.%m.%d')
    game.headers['Variant'] = 'From Position'
    game.headers['FEN'] = fen
    game.headers['Round'] = str(num)
    game.headers['White'] = white
    game.headers['Black'] = black

    node = None
    board = game.board()
    while not board.is_game_over():
        engine_suggestion = await engine.play(board, chess.engine.Limit(time=time_limit))
        suggested_move = str(engine_suggestion.move)
        if not node:
            node = game.add_variation(chess.Move.from_uci(suggested_move))
        else:
            node = node.add_variation(chess.Move.from_uci(suggested_move))
        board = node.board()


    await engine.quit()
    filename = f'../results/game_{num}.txt'
    result = board.outcome().winner
    if result == 1:
        outcome = 'White won'
        game.headers['Result'] = '1-0'
    elif result == 0:
        outcome = 'Black won'
        game.headers['Result'] = '0-1'
    elif result == None:
        outcome = 'It was a draw'
        game.headers['Result'] = '1/2-1/2'
        result = 0.5
    else:
        return 0
    print(f'{outcome}! Saving PGN on {filename}')
    game_output = open(filename, 'w')
    game_output.write(str(game))
    game_output.close()

    return result

