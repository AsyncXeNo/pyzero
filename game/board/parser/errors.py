from loguru import logger


class FenParserError(Exception):
    def __init__(self, *args: object) -> None:
        logger.error(args[0])
        super().__init__(*args)