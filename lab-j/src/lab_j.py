import pathlib
from os.path import join as pjoin

import numpy as np


def set_address(filename):
    script_folder = pathlib.Path(__file__).parent.resolve()
    data_dir = pjoin(script_folder, "../", "data")
    mat_fname = pjoin(data_dir, filename)

    return mat_fname


directions = ["N", "E", "S", "W"]


def turn_left(direction):
    return directions[(directions.index(direction) - 1) % 4]


def turn_right(direction):
    return directions[(directions.index(direction) + 1) % 4]


def main():

    # find T, D and M
    target = "T"
    for i in target:
        x, y = np.where(maze == target)

    # init
    direction = "S"
    x = int(x[0])
    y = int(y[0])
    not_d = True

    move_map = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1),
    }

    count = 0

    while not_d:
        if count > 100:
            warnings.warn("This is a custom warning from lab-h.", MyWarning)

        print(f"pos=({x},{y}), cell={maze[x, y]}, direction={direction}")

        dx, dy = move_map[direction]
        next_x = x + dx
        next_y = y + dy

        if maze[next_x, next_y] == "W":
            direction = turn_left(direction)
            print("front one is wall")
        else:
            if maze[next_x, next_y] == "P":
                print("front one is path")
                dx_temp, dy_temp = move_map[turn_left(direction)]
                if maze[x + dx_temp, y + dy_temp] == "P":
                    print("left one is path")
                    direction = turn_left(direction)

                else:
                    print("left one is not path")

            dx, dy = move_map[direction]
            x = x + dx
            y = y + dy
            count += 1

        if maze[x, y] == "D":
            not_d = False

        print(count)


if __name__ == "__main__":
    # read the file

    fname = set_address("maze.txt")

    with open(fname) as f:
        lines = f.readlines()

    # convert txt into list
    data = []
    for i in lines:
        data.append(i.split())

    maze = np.array(data)
    print(maze)

    main()
