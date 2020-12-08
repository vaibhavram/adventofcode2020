def pair_product(filename, tot):
    file = open(filename, "r")
    value_set = set([int(s) for s in file.readlines()])

    for value in value_set:
        if tot - value in value_set:
            return(value * (tot - value))

ans = pair_product("day1.csv", 2020)
print(ans)