import pyxel
import random

WIDTH = 128
HEIGHT = 128
SIZE = 64
SCALE = WIDTH // SIZE

NEIGHBORS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

grid_state = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
next_state = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


def init_grid():
    for y in range(SIZE):
        for x in range(SIZE):
            grid_state[y][x] = random.choice([0, 1])


def count_alive(x, y):
    count = 0
    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            count += grid_state[ny][nx]
    return count


def update_cells():
    for y in range(SIZE):
        for x in range(SIZE):
            alive_neighbors = count_alive(x, y)
            if grid_state[y][x] == 1:
                next_state[y][x] = 1 if 2 <= alive_neighbors <= 3 else 0
            else:
                next_state[y][x] = 1 if alive_neighbors == 3 else 0

    for y in range(SIZE):
        for x in range(SIZE):
            grid_state[y][x] = next_state[y][x]


def draw_cells():
    pyxel.cls(0)
    for y in range(SIZE):
        for x in range(SIZE):
            if grid_state[y][x] == 1:
                pyxel.rect(x * SCALE, y * SCALE, SCALE, SCALE, 11)


def update():
    if pyxel.btnp(pyxel.KEY_R):
        init_grid()
    update_cells()


def draw():
    draw_cells()


def setup_game():
    pyxel.init(WIDTH, HEIGHT, fps=30)
    pyxel.title = "Game of Life"
    init_grid()
    pyxel.run(update, draw)


if __name__ == "__main__":
    setup_game()
