import sys
import re

def get_data(filename):
    file = open(filename, "r")
    lines = file.readlines()
    time = int(re.sub("\n", "", lines[0]))
    buses = [e for e in re.sub("\n", "", lines[1]).split(",")]
    return (time, buses)

def get_interval(time, bus):
    return 0 if time % bus == 0 else bus * ((time // bus) + 1) - time

def get_next_bus(time, buses):
    numbered_buses = [int(bus) for bus in buses if bus != "x"]
    intervals = []
    for bus in numbered_buses:
        intervals.append(get_interval(time, bus))
    return numbered_buses[intervals.index(min(intervals))] * min(intervals)

# credit - https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfth69h/?utm_source=reddit&utm_medium=web2x&context=3
def get_earliest_timestamp(time, buses):
    indices = [(int(buses[i]), i) for i in range(len(buses)) if buses[i] != "x"]
    lcm = 1
    time = 0
    for i in range(len(indices) - 1):
        next_bus = indices[i+1][0]
        next_bus_lag = indices[i+1][1]
        lcm *= indices[i][0]
        while (time + next_bus_lag) % next_bus != 0:
            time += lcm
    return time

def main(filename):
    time, buses = get_data(filename)
    next_bus = get_next_bus(time, buses)
    earliest_timestamp = get_earliest_timestamp(time, buses)
    print(next_bus, earliest_timestamp)

main(sys.argv[1])