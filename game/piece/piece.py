from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.board.sqaure import Square

from game.utils.math.vector import Vector2


class Piece():
    def __init__(self, color: int, directions: list[Vector2] = [], range: int = 0) -> None:
        self.color: int = color
        self.directions: list[Vector2] = directions
        self.range: int = range

    def __str__(self) -> str:
        return self.__class__.__name__[0].upper()
    
    def get_moves(self, square: Square, squares: dict[tuple[int, int], Square]) -> list[Square]:
        moves: list[Square] = []
        current_pos: Vector2 = square.pos

        for direction in self.directions:
            for step in range(1, self.range+1):

                target_pos: Vector2 = current_pos.add(direction.scale(step))
                if target_pos.x < 0 or target_pos.x > 7 or target_pos.y < 0 or target_pos.y > 7:
                    break
                
                target_square: Square = squares[(target_pos.x, target_pos.y)]
                
                if target_square.piece is None:
                    moves.append(target_square)
                    continue

                if target_square.piece.color != self.color:
                    moves.append(target_square)
                break

        return moves


class Rook(Piece):
    def __init__(self, color: int) -> None:
        super().__init__(color,
                         directions=[
                             Vector2(1, 0),
                             Vector2(0, 1),
                             Vector2(-1, 0),
                             Vector2(0, -1)
                         ],
                         range=7)


class Knight(Piece):
    def __init__(self, color: int) -> None:
        super().__init__(color,
                         directions=[
                             Vector2(1, 2),
                             Vector2(2, 1),
                             Vector2(2, -1),
                             Vector2(1, -2),
                             Vector2(-1, -2),
                             Vector2(-2, -1),
                             Vector2(-2, 1),
                             Vector2(-1, 2)
                         ],
                         range=1)

    def __str__(self) -> str:
        return 'N'


class Bishop(Piece):
    def __init__(self, color: int) -> None:
        super().__init__(color,
                         directions=[
                             Vector2(1, 1),
                             Vector2(1, -1),
                             Vector2(-1, -1),
                             Vector2(-1, 1)
                         ],
                         range=7)


class Queen(Piece):
    def __init__(self, color: int) -> None:
        super().__init__(color,
                         directions=[
                             Vector2(1, 1),
                             Vector2(1, -1),
                             Vector2(-1, -1),
                             Vector2(-1, 1),
                             Vector2(1, 0),
                             Vector2(0, 1),
                             Vector2(-1, 0),
                             Vector2(0, -1)
                         ],
                         range=7)


class King(Piece):
    def __init__(self, color: int) -> None:
        super().__init__(color,
                         directions=[
                             Vector2(1, 1),
                             Vector2(1, -1),
                             Vector2(-1, -1),
                             Vector2(-1, 1),
                             Vector2(1, 0),
                             Vector2(0, 1),
                             Vector2(-1, 0),
                             Vector2(0, -1)
                         ],
                         range=1)


class Pawn(Piece):
    """
    Pawn is a complicated piece, so we will not use directions and range in this class.
    """

    def __init__(self, color: int) -> None:
        super().__init__(color)

    def get_moves(self, square: Square, squares: dict[tuple[int, int], Square]) -> list[Square]:
        moves: list[Square] = []

        direction: int = -1 if self.color == 0 else 1
        move_range: int = 2 if square.pos.y in [1, 6] else 1
        
        current_pos: Vector2 = square.pos

        # Moves to the front
        for step in range(1, move_range+1):
            target_pos: Vector2 = current_pos.add(Vector2(0, direction * step))
            target_square: Square = squares[(target_pos.x, target_pos.y)]
            if target_square.piece:
                break
            moves.append(target_square)

        # Captures
        left_capture: Vector2 = current_pos.add(Vector2(-1, direction))
        left_capture_square: Square | None = squares[(left_capture.x, left_capture.y)] if 8 < left_capture.x > 0 else None 
        right_capture: Vector2 = current_pos.add(Vector2(1, direction))
        right_capture_square: Square | None = squares[(right_capture.x, right_capture.y)] if 8 < right_capture.x > 0 else None

        for sq in (left_capture_square, right_capture_square):
            if sq is None: continue
            if (sq.piece and sq.piece.color != self.color) or (sq.is_ent()):
                moves.append(sq)

        return moves