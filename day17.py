import sys
import re

def get_init_slice(filename):
    file = open(filename, "r")
    return {0: [[char for char in re.sub("\n", "",line)] for line in file.readlines()]}

def get_num_neighbors(cubes, z, x, y):
    num_neighbors = 0
    for zz in [z - 1, z, z + 1]:
        if zz in cubes:
            for xx in [elem for elem in [x - 1, x, x + 1] if elem >= 0]:
                for yy in [elem for elem in [y - 1, y, y + 1] if elem >= 0]:
                    try:
                        num_neighbors += (1 if is_active(cubes, zz, xx, yy) else 0)
                        # print("looking at x = ", xx, ", y = ", yy, ", z = ", zz, " - ", cubes[zz][xx][yy])
                    except IndexError:
                        pass
    return num_neighbors - (1 if cubes[z][x][y] == "#" else 0) 

def is_active(cubes, z, x, y):
    return cubes[z][x][y] == "#"

def expand_cubes(init_cubes):
    z_abs = max(init_cubes.keys())
    x_dim = len(init_cubes[0])
    y_dim = len(init_cubes[0][0])
    for zz in range(-z_abs, z_abs + 1):
        for i in range(len(init_cubes[zz])):
            init_cubes[zz][i] = ["."] + init_cubes[zz][i] + ["."]
        init_cubes[zz] = [["."] * (y_dim + 2)] + init_cubes[zz] + [["."] * (y_dim + 2)]
    for zz in [z_abs + 1, -z_abs - 1]:
        init_cubes[zz] = []
        for k in range(x_dim + 2):
            init_cubes[zz].append(["."] * (y_dim + 2))

def find_changes(cubes):
    expand_cubes(cubes)
    z_abs = max(cubes.keys())
    x_dim = len(cubes[0])
    y_dim = len(cubes[0][0])
    changes = {}
    for zz in range(-z_abs, z_abs + 1):
        for xx in range(x_dim):
            for yy in range(y_dim):
                # if zz == 0:
                #         print(zz, xx, yy, get_num_neighbors(cubes, zz, xx, yy))
                if not is_active(cubes, zz, xx, yy) and get_num_neighbors(cubes, zz, xx, yy) == 3:
                    changes[(zz, xx, yy)] = "#"
                elif is_active(cubes, zz, xx, yy) and not 2 <= get_num_neighbors(cubes, zz, xx, yy) <= 3:
                    changes[(zz, xx, yy)] = "."
    return changes

def make_changes(cubes, changes):
    for z, x, y in changes:
        cubes[z][x][y] = changes[(z,x,y)]

def count_active(cubes):
    count = 0
    z_abs = max(cubes.keys())
    x_dim = len(cubes[0])
    y_dim = len(cubes[0][0])
    for zz in range(-z_abs, z_abs + 1):
        for xx in range(x_dim):
            for yy in range(y_dim):
                count += is_active(cubes, zz, xx, yy)
    return count

def print_cubes(cubes):
    z_abs = max(cubes.keys())
    for zz in range(-z_abs, z_abs + 1):
        # if zz == 0:
        print("z =", zz)
        for xx in range(len(cubes[zz])):
            print("".join(cubes[zz][xx]))
        print("-------------------------")

def iterate_cube(cubes, steps):
    while steps > 0:
        # print_cubes(cubes)
        changes = find_changes(cubes)
        make_changes(cubes, changes)
        steps -= 1
    return count_active(cubes)

def main(filename):
    init_slice = get_init_slice(filename)
    num_active = iterate_cube(init_slice, 6)
    print(num_active)

main(sys.argv[1])