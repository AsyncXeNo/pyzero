
INDEX_TO_FILE: dict[int, str] = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}
FILE_TO_INDEX: dict[str, int] = { file: index for (index, file) in INDEX_TO_FILE.items() }

INDEX_TO_RANK: dict[int, str] = {
    0: '1',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8'
}
RANK_TO_INDEX: dict[str, int] = { rank: index for (index, rank) in INDEX_TO_RANK.items() }