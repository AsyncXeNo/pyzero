import config as _

from loguru import logger

from game.board.board import Board


def main():
    
    logger.debug('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    logger.debug(Board.from_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1').to_fen())


if __name__ == '__main__':
    main()