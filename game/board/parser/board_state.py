from game.board.parser.errors import FenParserError


class BoardStateParser(object):
    def __init__(self, source: str) -> None:

        self.source: str = source
        self.file: int = 0
        self.rank: int = 7

        self.board_state: dict[tuple[int, int], str] = {}

    """
    MAIN
    """

    def get_board_state(self) -> dict[tuple[int, int], str]:
        self.board_state = {}

        for char in self.source:
            self.__process(char)

        return self.board_state

    def __process(self, char: str) -> None:
        if char == '/':
            self.__advance_rank()
        if char.isalpha():
            if char.lower() not in 'rnbqkp':
                raise FenParserError('Invalid board-state in FEN string')
            self.board_state[(self.file, self.rank)] = char
            self.__advance_file()
        if char.isdigit():
            for _ in range(int(char)):
                self.__advance_file()

    """
    HELPERS
    """

    def __is_at_end(self) -> bool:
        return self.rank < 0

    def __advance_file(self) -> None:
        self.file += 1

    def __advance_rank(self) -> None:
        self.rank -= 1
        self.file = 0
        if self.__is_at_end():
            raise FenParserError('Invalid board-state in FEN string')
