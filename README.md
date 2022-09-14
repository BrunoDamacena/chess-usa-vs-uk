# Chess: USA vs the UK
So, I programmed Stockfish 15 to play against itself. The only caveat is that one player is USA (starts without rooks) and the other one is UK (starts without a Queen). This means the USA doesn't have the capability of castling.

This code in Python goes through 200 games, 100 where the USA plays the white pieces, and another 100 when the UK plays the white pieces. The goal is to see who is stronger. 

## Results
- When the USA was playing white, out of 100 matches, the USA won 85 times, the UK won 1 time, and 14 matches resulted in a draw.
- When the USA was playing black, out of 100 matches, the USA won 65 times, the UK won 7 times, and 28 matches resulted in a draw.

### Conclusion
Apparently, it is advantageous to have a Queen instead of two Rooks.