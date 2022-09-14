import asyncio
from stockfish import play_game
import chess.engine

def main():
    asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
    time_per_move = 0.1 # time in seconds that stockfish have to call a move
    usa_white = []
    usa_black = []
    # USA is white
    for i in range(100):
        result = asyncio.run(play_game(usa_color='white', time_limit=time_per_move, num=i+1))
        usa_white.append(result)

    # USA is black
    for i in range(100,200):
        result = asyncio.run(play_game(usa_color='black', time_limit=time_per_move, num=i+1))
        usa_black.append(result)

    print(f'When USA was playing white, out of 100 matches, USA won {usa_white.count(1)} times, UK won {usa_white.count(0)} times, and {usa_white.count(0.5)} matches resulted on a draw.')
    print(f'When USA was playing black, out of 100 matches, USA won {usa_black.count(0)} times, UK won {usa_black.count(1)} times, and {usa_black.count(0.5)} matches resulted on a draw.')


if __name__ == '__main__':
    main()