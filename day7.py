import sys
import re

class Bag:
    def __init__(self, name):
        self.name = name 
        self.contents = {}
        self.parents = set()

    def __repr__(self):
        return self.name + ": " + str(self.contents)

    def add_content(self, content_bag, content_number):
        self.contents[content_bag] = content_number

    def add_parent(self, parent_bag):
        self.parents.add(parent_bag)

    def num_parents(self):
        return len(self.parents)

    def get_parents(self):
        return self.parents

    def num_contents(self):
        return len(self.contents)

    def get_content_bags(self):
        return self.contents.keys()

    def num_content_bag(self, content_bag):
        return self.contents[content_bag]

def get_bags(filename):
    file = open(filename, "r")
    bags = {}
    lines = file.readlines()
    for line in lines:
        parts = re.sub("\\.", "", re.sub("\n", "", line)).split(" contain ")
        name = parts[0][:-5]
        bags[name] = Bag(name)
    for line in lines:
        parts = re.sub("\\.", "", re.sub("\n", "", line)).split(" contain ")
        name = parts[0][:-5]
        sub_bags = parts[1].split(", ")
        contents = {}
        for sub_bag in sub_bags:
            if re.match("[0-9]", sub_bag):
                number = int(sub_bag[0])
                sub_bag_name = sub_bag[2:]
                if number != 1:
                    sub_bag_name = sub_bag_name[:-5]
                else:
                    sub_bag_name = sub_bag_name[:-4]
                bags[name].add_content(bags[sub_bag_name], number)
                bags[sub_bag_name].add_parent(bags[name])
    file.close()
    return bags

def get_ultimate_parents(bag):
    if bag.num_parents() == 0:
        return set()
    else:
        return_set = set()
        for parent in bag.get_parents():
            # print(parent.name, "-", bag.name)
            return_set.add(parent.name)
            return_set = return_set.union(get_ultimate_parents(parent))
        return return_set

def get_num_ultimate_parents(bag):
    return len(get_ultimate_parents(bag))

def get_num_content_bags(bag):
    if bag.num_contents() == 0:
        return 0
    else:
        return \
        sum([bag.num_content_bag(content_bag) for content_bag in bag.get_content_bags()]) + \
        sum([bag.num_content_bag(content_bag) * get_num_content_bags(content_bag) for content_bag in bag.get_content_bags()])

def main(filename):
    bags = get_bags(filename)
    ultimate_parents = get_num_ultimate_parents(bags['shiny gold'])
    num_children = get_num_content_bags(bags['shiny gold'])
    print(ultimate_parents, num_children)

main(sys.argv[1])