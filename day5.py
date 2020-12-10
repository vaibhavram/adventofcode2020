import sys
import re

def get_tickets(filename):
    file = open(filename, "r")
    tickets = [re.sub("\n", "", ticket) for ticket in file.readlines()]
    file.close()
    return tickets

def get_index(arr, min_row_range, max_row_range, descend, ascend):
    if len(arr) == 1:
        if arr[0] == descend:
            return min_row_range
        elif arr[0] == ascend:
            return max_row_range
    else:
        if arr[0] == descend:
            new_max = min_row_range + (max_row_range - min_row_range - 1) // 2
            return get_index(arr[1:], min_row_range, new_max, descend, ascend)
        elif arr[0] == ascend:
            new_min = max_row_range - (max_row_range - min_row_range - 1) // 2
            return get_index(arr[1:], new_min, max_row_range, descend, ascend)

def get_seat_id(ticket):
    row = ticket[0:7]
    column = ticket[-3:]
    row_index = get_index(row, 0, 127, "F", "B")
    col_index = get_index(column, 0, 7, "L", "R")
    return 8 * row_index + col_index

def get_seat_ids(tickets):
    return [get_seat_id(ticket) for ticket in tickets]

def get_max_seat_id(tickets):
    return max(get_seat_ids(tickets))

def get_missing_seat_ids(tickets):
    max_id = get_max_seat_id(tickets)
    seat_ids = get_seat_ids(tickets)
    for i in range(0, max_id):
        if i not in seat_ids:
            print(i)

def main(filename):
    tickets = get_tickets(filename)
    max_seat_id = get_max_seat_id(tickets)
    print(max_seat_id)
    print("---")
    get_missing_seat_ids(tickets)

main(sys.argv[1])