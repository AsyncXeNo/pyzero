from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.piece.piece import Piece

from game.board.constants import INDEX_TO_FILE, INDEX_TO_RANK
from game.utils.math.vector import Vector2


class Square(object):
    def __init__(self, file: int, rank: int, piece: Piece | None = None, ent: bool = False) -> None:
        self.pos: Vector2 = Vector2(file, rank)
        self.piece: Piece | None = piece
        self.ent: bool = ent

    def is_ent(self) -> bool:
        return self.ent
    
    def set_ent(self, ent: bool) -> None:
        self.ent = ent

    def set_piece(self, piece: Piece) -> None:
        self.piece = piece

    def remove_piece(self) -> Piece | None:
        """Removes the piece from the square and returns it"""
        
        piece: Piece | None = self.piece
        self.piece = None
        return piece
    
    def __str__(self) -> str:
        return f'{INDEX_TO_FILE[self.pos.x]}{INDEX_TO_RANK[self.pos.y]}'
    
    def __repr__(self) -> str:
        return self.__str__()