import sys

def get_passwords(filename):
    file = open(filename, "r")
    passwords = [pw for pw in file.readlines()]
    return passwords

def check_rule(password_rule):
    split = password_rule.split(" ")
    nums = [int(e) for e in split[0].split("-")]
    char_rule = split[1].split(":")[0]
    char_value = 0
    for char in split[2]:
        char_value += char == char_rule
        if char_value > nums[1]:
            return False
    return char_value >= nums[0]

def check_passwords(passwords):
    return sum([check_rule(pw) for pw in passwords])

def main(filename):
    passwords = get_passwords(filename)
    print(check_passwords(passwords))

main(sys.argv[1])