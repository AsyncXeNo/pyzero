from __future__ import annotations

from game.board.sqaure import Square
from game.piece.piece import Rook, Knight, Bishop, Queen, King, Pawn, Piece
from game.board.board import Board
from game.board.constants import FILE_TO_INDEX, RANK_TO_INDEX
from game.board.parser.errors import FenParserError
from game.board.parser.board_state import BoardStateParser


class FenParser(object):
    
    @staticmethod
    def parse(fen: str) -> Board:
        """
        Parses a raw FEN string into a Board instance
        """
        
        fields = fen.split(' ')
        if len(fields) != 6:
            raise FenParserError('Invalid FEN string')
        
        # Side to move
        try: side_to_move: int = { 'w': 1, 'b': 0 }[fields[1]]
        except KeyError: raise FenParserError('Invalid side-to-move in FEN string')
        
        # Halfmove clock
        try: half_moves: int = int(fields[4])
        except ValueError: raise FenParserError('Invalid half-move in FEN string')

        # Fullmove number
        try: full_moves: int = int(fields[5])
        except ValueError: raise FenParserError('Invalid full-move in FEN string')

        # Board State
        board_state: dict[tuple[int, int], str] = BoardStateParser(fields[0]).get_board_state()
        squares: dict[tuple[int, int], Square] = {}
        pieces: list[Piece] = []

        for rank in range(8):
            for file in range(8):
                piece: Piece | None = None
                if p := board_state.get((file, rank)):
                    color: int = int(p.isupper())
                    piece = {
                        'r': Rook,
                        'n': Knight,
                        'b': Bishop,
                        'q': Queen,
                        'k': King,
                        'p': Pawn
                    }[p.lower()](color)
                    pieces.append(piece)

                squares[(file, rank)] = Square(file, rank, piece)

        # Castling state
        castling_state_fen: str = fields[2]

        if len(castling_state_fen) > 4 or not all([c in 'kqKQ-' for c in castling_state_fen]):
            raise FenParserError('Invalid castling-state in FEN string')

        castling_state: dict[int, list[int]] = {
            0: [False, False],
            1: [False, False]
        } # { color: [kingside, queenside] }
        
        if 'k' in castling_state_fen:
            castling_state[0][0] = True
        if 'q' in castling_state_fen:
            castling_state[0][1] = True
        if 'K' in castling_state_fen:
            castling_state[1][0] = True
        if 'Q' in castling_state_fen:
            castling_state[1][1] = True

        # En Passant Target Square
        ent_square_fen: str = fields[3]

        if len(ent_square_fen) > 2:
            raise FenParserError('Invalid en-passant-target-square in FEN string')

        ent_square: Square | None = None

        if ent_square_fen != '-':
            try:
                ent_square = squares[(
                    FILE_TO_INDEX[ent_square_fen[0]],
                    RANK_TO_INDEX[ent_square_fen[1]]
                )]
            except (ValueError, IndexError):
                raise FenParserError('Invalid en-passant-target-square in FEN string')
            
        return Board(
            squares,
            pieces,
            side_to_move,
            castling_state,
            ent_square,
            half_moves,
            full_moves
        )
