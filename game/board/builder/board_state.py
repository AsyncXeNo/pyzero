from game.board.sqaure import Square


class BoardStateBuilder(object):
    def __init__(self, squares: dict[tuple[int, int], Square]) -> None:
        self.squares: dict[tuple[int, int], Square] = squares
        self.file: int = -1
        self.rank: int = 7

        self.empty_count: int = 0

        self.board_state_str: str = ''

    """
    MAIN
    """

    def build_board_state(self) -> str:
        self.board_state_str = ''

        while not self.__is_at_end():
            square: Square = self.squares[self.__advance()]
            self.__process(square)

        return self.board_state_str

    def __process(self, square: Square) -> None:
        if square.piece is not None:
            if self.empty_count > 0:
                self.board_state_str += str(self.empty_count)
                self.empty_count = 0
            symbol: str = str(square.piece)
            symbol = symbol.lower() if square.piece.color == 0 else symbol
            self.board_state_str += symbol
        else:
            self.empty_count += 1

    """
    HELPERS
    """

    def __is_at_end(self) -> bool:
        return self.rank <= 0 and self.file >= 7
    
    def __advance(self) -> tuple[int, int]:
        self.file += 1
        if self.file > 7:
            if self.empty_count > 0:
                self.board_state_str += str(self.empty_count)
                self.empty_count = 0
            if self.rank > 0:
                self.board_state_str += '/'
            self.rank -= 1
            self.file = 0
        return self.file, self.rank