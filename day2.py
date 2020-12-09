import sys

def get_passwords(filename):
    file = open(filename, "r")
    passwords = [pw for pw in file.readlines()]
    file.close()
    return passwords

def password_parse(password_rule):
    split = password_rule.split(" ")
    nums = [int(e) for e in split[0].split("-")]
    char = split[1].split(":")[0]
    return((int(nums[0]), int(nums[1]), char, split[2]))

def check_rule1(parse):
    count = 0
    for char in parse[3]:
        count += char == parse[2]
        if count > parse[1]:
            return False
    return count >= parse[0]

def check_rule2(parse):
    count = 0
    first_match = parse[3][parse[0]-1] == parse[2]
    second_match = parse[3][parse[1]-1] == parse[2]
    return(first_match + second_match == 1)

def check_passwords(passwords, rule_checker):
    return sum([rule_checker(password_parse(pw)) for pw in passwords])

def main(filename):
    passwords = get_passwords(filename)
    rule1 = check_passwords(passwords, check_rule1)
    rule2 = check_passwords(passwords, check_rule2)
    print(rule1, rule2)

main(sys.argv[1])