import sys
import re

def get_form_groups(filename):
    file = open(filename, "r")
    form_groups = []
    curr_form_group = []
    for line in file.readlines():
        if line == "\n":
            form_groups.append(curr_form_group)
            curr_form_group = []
        else:
            curr_form_group.append(re.sub("\n", "", line))
    file.close()
    if curr_form_group:
        form_groups.append(curr_form_group)
    return(form_groups)

def get_uniq_questions(form_group):
    uniq_questions = set()
    for form in form_group:
        for char in form:
            uniq_questions.add(char)
    return len(uniq_questions)

def get_complete_questions(form_group):
    group_size = len(form_group)
    questions_ans = {}
    for form in form_group:
        for char in form:
            questions_ans[char] = questions_ans.get(char, 0) + 1
    return sum([count == group_size for count in questions_ans.values()])

def sum_questions(form_groups, group_func):
    return sum([group_func(form_group) for form_group in form_groups])

def main(filename):
    form_groups = get_form_groups(filename)
    total_uniq_questions = sum_questions(form_groups, get_uniq_questions)
    total_complete_questions = sum_questions(form_groups, get_complete_questions)
    print(total_uniq_questions, total_complete_questions)

main(sys.argv[1])