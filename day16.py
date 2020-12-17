import sys
import re

def get_data(filename):
    file = open(filename, "r")
    reqs = {}
    num_empty_lines = 0
    while num_empty_lines == 0:
        line = file.readline()
        if line == "\n":
            num_empty_lines += 1
        else:
            line = re.sub("\n", "", line).split(": ")
            reqs[line[0]] = []
            ranges = line[1].split(" or ")
            for rg in ranges:
                reqs[line[0]].append([int(elem) for elem in rg.split("-")])
    file.readline()

    my_ticket = [int(item) for item in re.sub("\n", "", file.readline()).split(",")]
    file.readline()
    
    nearby_tickets = []
    file.readline()
    line = file.readline()
    while line:
        nearby_tickets.append([int(item) for item in re.sub("\n", "", line).split(",")])
        line = file.readline()
    return (reqs, my_ticket, nearby_tickets)

def merge_intervals(reqs):
    intervals = []
    for k in reqs:
        intervals.append(reqs[k][0].copy())
        intervals.append(reqs[k][1].copy())
    intervals = sorted(intervals)
    result = []
    for interval in intervals:
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        elif interval[1] > result[-1][1]:
            result[-1][1] = interval[1]
    return result

def get_ticket_scanning_error_rate(reqs, tickets):
    interval = merge_intervals(reqs)
    tot = 0
    for ticket in tickets:
        tot += sum([d for d in ticket if not any([i[0] <= d <= i[1] for i in interval])])
    return tot

def is_valid(ticket, intervals):
    in_interval = [False] * len(ticket)
    for i in intervals:
        temp = [i[0] <= d <= i[1] for d in ticket]
        in_interval = [in_interval[i] or temp[i] for i in range(len(ticket))]
    return all(in_interval)

def find_corresponding_fields(reqs, tickets):
    intervals = merge_intervals(reqs)
    valid_tickets = []
    for ticket in tickets:
        if is_valid(ticket, intervals):
            valid_tickets.append(ticket)
    positions = {}
    for pos in range(len(tickets[0])):
        fields = {}
        for ticket in valid_tickets:
            for req in reqs:
                if is_valid([ticket[pos]], reqs[req]):
                    fields[req] = fields.get(req, 0) + 1
        positions[pos] = [key for key in fields if fields[key] == len(valid_tickets)]
    while not all([len(positions[pos]) == 1 for pos in positions]):
        for pos in positions:
            if len(positions[pos]) == 1:
                for pos2 in positions:
                    if pos2 != pos:
                        try:
                            positions[pos2].remove(positions[pos][0])
                        except ValueError:
                            pass
    return {positions[key][0]:key for key in positions}

def get_my_ticket_departure_value(reqs, my_ticket, nearby_tickets):
    fields = find_corresponding_fields(reqs, nearby_tickets)
    prod = 1
    for field in fields:
        if field.startswith("departure"):
            prod *= my_ticket[fields[field]]
    return prod

def main(filename):
    reqs, my_ticket, nearby_tickets = get_data(filename)
    ticket_scanning_error_rate = get_ticket_scanning_error_rate(reqs, nearby_tickets)
    ticket_departure_value = get_my_ticket_departure_value(reqs, my_ticket, nearby_tickets)
    print(ticket_scanning_error_rate, ticket_departure_value)

main(sys.argv[1])