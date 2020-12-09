import sys
import re

def get_passports(filename):
    file = open(filename, "r")
    passports = []
    curr_passport = {}
    for line in file.readlines():
        if line == "\n":
            passports.append(curr_passport)
            curr_passport = {}
        else:
            items = line[0:(len(line) - 1)].split(" ")
            for item in items:
                kv = item.split(":")
                curr_passport[kv[0]] = kv[1]
    file.close()
    if curr_passport:
        passports.append(curr_passport)
    print(passports[0])
    return(passports)

def valid_passport1(passport):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([field in passport for field in req_fields])

def valid_height(height):
    if len(height) < 4:
        return False
    else:
        ht_unit = height[-2:]
        ht_value = int(height[:-2])
        return (ht_unit == "cm" and 150 <= ht_value <= 193) or (ht_unit == "in" and 59 <= ht_value <= 76)

def valid_passport2(passport):
    if not valid_passport1(passport):
        return False
    else:
        valid = []
        valid.append(1920 <= int(passport["byr"]) <= 2002)
        valid.append(2010 <= int(passport["iyr"]) <= 2020)
        valid.append(2020 <= int(passport["eyr"]) <= 2030)
        valid.append(valid_height(passport["hgt"]))
        valid.append(bool(re.match("^#[0-9a-f]{6}$", passport["hcl"])))
        valid.append(passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        valid.append(bool(re.match("^[0-9]{9}$", passport["pid"])))
        return all(valid)
        # return valid

def count_valid_passports(passports, validity_func):
    return sum([validity_func(passport) for passport in passports])

# def find_discrepancies(passports):
#     order = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
#     for passport in passports:
#         valid2 = valid_passport2(passport)
#         if valid_passport1(passport) and not all(valid2):
#             for i in range(len(valid2)):
#                 if not valid2[i]:
#                     print(order[i], passport[order[i]])

def main(filename):
    passports = get_passports(filename)
    # find_discrepancies(passports)
    num_valid_passports1 = count_valid_passports(passports, valid_passport1)
    num_valid_passports2 = count_valid_passports(passports, valid_passport2)
    print(num_valid_passports1, num_valid_passports2)

main(sys.argv[1])