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
    facing_direction = directions["E"]
    position = [0,0]
    for step in instructions:
        if step[0] in directions.keys():
            position[0] += directions[step[0]][0] * step[1]
            position[1] += directions[step[0]][1] * step[1]
        elif step[0] in "LR":
            facing_degrees = (facing_degrees + step[1] * (-1 if step[0] == "R" else 1)) % 360
            facing_direction = directions[degrees[facing_degrees]]
        elif step[0] == "F":
            position[0] += facing_direction[0] * step[1]
            position[1] += facing_direction[1] * step[1]
    return abs(position[0]) + abs(position[1])

def rotate_about_origin(point, degrees):
    temp = [0,0]
    if degrees % 360 == 0:
        pass
    elif degrees % 360 == 90:
        temp[0] = -1 * point[1]
        temp[1] = point[0]
    elif degrees % 360 == 180:
        temp[0] = -1 * point[0]
        temp[1] = -1 * point[1]
    elif degrees % 360 == 270:
        temp[0] = point[1]
        temp[1] = -1 * point[0]
    return temp

def navigate_waypoint(instructions):
    directions = {"N": [0,1], "S": [0,-1], "E": [1,0], "W": [-1,0]}
    boat = [0,0]
    waypoint = [10,1]
    for step in instructions:
        if step[0] in directions.keys():
            waypoint[0] += directions[step[0]][0] * step[1]
            waypoint[1] += directions[step[0]][1] * step[1]
        elif step[0] in "LR":
            waypoint = rotate_about_origin(waypoint, (-1 if step[0] == "R" else 1) * step[1])
        elif step[0] == "F":
            boat[0] += step[1] * waypoint[0]
            boat[1] += step[1] * waypoint[1]
    return abs(boat[0]) + abs(boat[1])

def main(filename):
    instructions = get_instructions(filename)
    cardinal = navigate_cardinal(instructions)
    waypoint = navigate_waypoint(instructions)
    print(cardinal, waypoint)

main(sys.argv[1])