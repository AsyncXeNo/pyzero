from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.board.sqaure import Square
    from game.piece.piece import Piece


class Board(object):

    @staticmethod
    def from_fen(fen: str) -> Board:
        from game.board.parser.fen import FenParser
        return FenParser.parse(fen)
    
    def __init__(self, 
                 squares: dict[tuple[int, int], Square],
                 pieces: list[Piece],
                 side: int, 
                 castling_state: dict[int, list[int]],
                 ent_square: Square | None,
                 half_moves: int,
                 full_moves: int
                 ) -> None:

        self.squares: dict[tuple[int, int], Square] = squares
        self.pieces: list[Piece] = pieces
        self.side_to_move: int = side
        self.castling_state: dict[int, list[int]] = castling_state
        self.ent_square: Square | None
        self.set_ent_square(ent_square)
        self.half_moves: int = half_moves
        self.full_moves: int = full_moves

    def set_ent_square(self, square: Square | None) -> None:
        if self.ent_square: self.ent_square.set_ent(False)
        self.ent_square = square
        if self.ent_square: self.ent_square.set_ent(True)

    def to_fen(self) -> str:
        from game.board.builder.fen import FenBuilder
        return FenBuilder.build(self)

    def __str__(self) -> str:
        board: str = f'Side to move: {self.side_to_move} | Half moves: {self.half_moves} | Full moves: {self.full_moves} | Castling state: {self.castling_state} | ent_square: {self.ent_square}'
        for rank in range(7, -1, -1):
            rank_str: str = ''
            for file in range(8):
                square: Square = self.squares[(file, rank)]
                rank_str += f'{square.piece if square.piece else 0} '
            board += f'\n{rank_str}'
        return board