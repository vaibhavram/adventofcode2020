import sys
import re

def get_instructions(filename):
    file = open(filename, "r")
    instructions = [(line[0], int(re.sub("\n", "", line[1:]))) for line in file.readlines()]
    return instructions

def navigate_cardinal(instructions):
    directions = {"N": [0,1], "S": [0,-1], "E": [1,0], "W": [-1,0]}
    degrees = {0: "E", 90: "N", 180: "W", 270: "S"}
    facing_degrees = 0
    facing_direction = directions["E"] # degrees[facing_degrees]
    position = [0,0]
    for step in instructions:
        # print(position, facing_degrees)
        # print(step)
        if step[0] in directions.keys():
            position[0] += directions[step[0]][0] * step[1]
            position[1] += directions[step[0]][1] * step[1]
        elif step[0] in "LR":
            facing_degrees = (facing_degrees + step[1] * (-1 if step[0] == "R" else 1)) % 360
            facing_direction = directions[degrees[facing_degrees]]
        elif step[0] == "F":
            position[0] += facing_direction[0] * step[1]
            position[1] += facing_direction[1] * step[1]
        # print(position, facing_degrees)
        # print("---")
    return abs(position[0]) + abs(position[1])

def navigate_waypoint(instructions):
    pass

def main(filename):
    instructions = get_instructions(filename)
    manhattan = navigate_cardinal(instructions)
    print(manhattan)

main(sys.argv[1])