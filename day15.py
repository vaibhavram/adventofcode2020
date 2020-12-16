def play_game(starter, num_turns):
    last_pos = {}
    nums = []
    last2 = -1
    last1 = -1
    for i in range(num_turns):
        if i < len(starter):
            last2 = last1
            last1 = starter[i]
        elif last1 not in last_pos.keys():
            last2 = last1
            last1 = 0
        else:
            last2 = last1
            last1 = i - 1 - last_pos[last2]
        if last2 != -1:
            last_pos[last2] = i - 1
    return last1

def main():
    data = [0,12,6,13,20,1,17]
    n2020 = play_game(data, 2020)
    n30000000 = play_game(data, 30000000)
    print(n2020, n30000000)

main()