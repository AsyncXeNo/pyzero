from __future__ import annotations


class Vector2(object):
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

        
    def add(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)
    
    def subtract(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)
    
    def scale(self, scalar: int) -> Vector2:
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __str__(self) -> str:
        return f'Vector2({self.x}, {self.y})'