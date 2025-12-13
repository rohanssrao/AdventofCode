# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "polyomino",
# ]
# ///

from polyomino.board import Rectangle
from polyomino.tileset import Tileset

import signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

tiles = []

parsing_tiles = True

tile = []

boards = []
quantitieses = []

for line in open(0).read().splitlines():
    if ":" in line and "x" not in line:
        parsing_tiles = True
        continue
    if line == "":
        parsing_tiles = False
        tiles.append([
            (x, y)
            for x in range(len(tile))
            for y in range(len(tile[x]))
            if tile[x][y] == "#"
        ])
        tile = []
        continue
    if parsing_tiles:
        tile.append(line)
    else:
        boards.append(tuple(map(int, line.split(":")[0].split("x"))))
        quantitieses.append(tuple(map(int, line.split(" ")[1:])))


# for t in tiles:
#     print(t)
#
# print(boards)
#
# print(quantitieses)

from multiprocessing import Process
from time import sleep

def run_with_limited_time(func, args, kwargs, time):
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join(time)
    if p.is_alive():
        p.terminate()
        return False

    return True


for board, quantities in zip(boards, quantitieses):
    board = Rectangle(*board)
    tileset = [ [tiles[i]] * q for i, q in enumerate(quantities) if q != 0]
    tileset = [ t for tile in tileset for t in tile ]
    problem = board.tile_with_set(Tileset(tileset, [], [[(0, 0)]]))

    solution = run_with_limited_time(problem.solve, (), {}, 1)
    print(solution)
