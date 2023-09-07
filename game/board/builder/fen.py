from game.board.board import Board
from game.board.builder.board_state import BoardStateBuilder


class FenBuilder(object):
    
    @staticmethod
    def build(board: Board) -> str:
        """
        Generates a FEN string from a Board instance
        """

        # Board state
        board_state_fen: str = BoardStateBuilder(board.squares).build_board_state()

        # Castling state
        castling_state_fen: str = ''
        if board.castling_state[1][0]:
            castling_state_fen += 'K'
        if board.castling_state[1][1]:
            castling_state_fen += 'Q'
        if board.castling_state[0][0]:
            castling_state_fen += 'k'
        if board.castling_state[0][1]:
            castling_state_fen += 'q'
        castling_state_fen = castling_state_fen if castling_state_fen else '-'

        # En Passant Target Square
        ent_square_fen: str = '-'
        if board.ent_square is not None:
            ent_square_fen = str(board.ent_square)

        # Side to move
        side_to_move: str = 'w' if board.side_to_move == 1 else 'b'

        # Halfmove clock
        half_moves: str = str(board.half_moves)

        # Fullmove number
        full_moves: str = str(board.full_moves)

        # Full FEN string
        return f'{board_state_fen} {side_to_move} {castling_state_fen} {ent_square_fen} {half_moves} {full_moves}'