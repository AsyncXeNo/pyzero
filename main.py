import config as _

from game.board.board import Board
from game.move import Move

from fentoboardimage import fenToImage, loadPiecesFolder


def main():
    board: Board = Board.from_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    move1: Move = Move(board,
                       [
                           (
                            (0, 1),
                            (0, 6)
                           )
                       ],
                       1)    
    move2: Move = Move(board,
                       [
                           (
                            (0, 6),
                            (1, 7)
                           )
                       ],
                       1)

    fenToImage(
        fen=board.to_fen(),
        squarelength=100,
        pieceSet=loadPiecesFolder('./res/pieces'),
        darkColor='#D18B47',
        lightColor='#FFCE9E'
    ).show()

    move1.do()
    
    fenToImage(
        fen=board.to_fen(),
        squarelength=100,
        pieceSet=loadPiecesFolder('./res/pieces'),
        darkColor='#D18B47',
        lightColor='#FFCE9E'
    ).show()

    move2.do()
    
    fenToImage(
        fen=board.to_fen(),
        squarelength=100,
        pieceSet=loadPiecesFolder('./res/pieces'),
        darkColor='#D18B47',
        lightColor='#FFCE9E'
    ).show()

    move2.undo()
    
    fenToImage(
        fen=board.to_fen(),
        squarelength=100,
        pieceSet=loadPiecesFolder('./res/pieces'),
        darkColor='#D18B47',
        lightColor='#FFCE9E'
    ).show()

    move1.undo()
    
    fenToImage(
        fen=board.to_fen(),
        squarelength=100,
        pieceSet=loadPiecesFolder('./res/pieces'),
        darkColor='#D18B47',
        lightColor='#FFCE9E'
    ).show()


if __name__ == '__main__':
    main()