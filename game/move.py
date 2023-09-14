from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.board.board import Board
    from game.board.sqaure import Square
    from game.piece.piece import Piece


class Move(object):
    def __init__(self, board: Board, moves: list[tuple[tuple[int, int], tuple[int, int]]], color: int) -> None:
        self.board: Board = board
        self.moves: list[tuple[Square, Square]] = [(board.squares[source], board.squares[target]) for source, target in moves]
        self.color: int = color
        self.target_pieces: list[Piece | None] = [target.piece for _, target in self.moves]

    """
    MAIN
    """

    def do(self) -> None:
        for source, target in self.moves:
            self.board.move_piece(source, target)

    def undo(self) -> None:
        for i, (source, target) in enumerate(self.moves):
            self.board.move_piece(target, source)
            target.set_piece(self.target_pieces[i])

    """
    HELPERS
    """
    
    # @staticmethod
    # def from_notation(board: Board) -> Move:
    #     pass