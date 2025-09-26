'''
Can you derive problem statement from the solution code below?
def mismatches(records):
    # create stack for each person
    # on enter, add to paul's stack
    # on exit, see if stack is not empty and then pop it
    # How to hold each person's stack?
    mis_entries = []
    mis_exits = []
    per_dict = {}
    for rec in records:
        per, state = rec[0], rec[1]
        per_stack = []
        if per in per_dict:
            per_stack = per_dict.get(per)
        else:
            per_dict[per] = per_stack
        if state == 'enter':
            if per_stack == []:
                per_stack.append('enter')
                per_dict[per] = per_stack
            else:
                if per not in mis_entries:
                    mis_entries.append(per);
        else: # exit
            if per_stack == []:
                if per not in mis_exits:
                    mis_exits.append(per);
            else:
                per_stack.pop()
                per_dict[per] = per_stack
                
    for per in per_dict:
        per_stack = per_dict.get(per)
        if per_stack != []:
            item = per_stack.pop()
            if item == 'enter':
                if per not in mis_entries:
                    mis_entries.append(per);
            else:
                if per not in mis_exits:
                    mis_exits.append(per);
    return [mis_entries, mis_exits]
    
# Test case
records = [["Paul", "enter"], ["Paul", "enter"], ["Paul", "exit"], ["Paul", "exit"], ["Paul", "exit"]]
print(mismatches(records))  # Output: [["Paul"], []]   

Problem Statement:
Given a list of records containing the name of a person and their entry/exit state, identify any mismatches in their entry and exit logs. 
A mismatch occurs when a person has an "enter" log without a corresponding "exit" log, or vice versa. 
The output should be a list of persons with mismatched entries and exits.

Build a better solution if possible. 
'''

def mismatches(records):
    # create stack for each person
    # on enter, add to paul's stack
    # on exit, see if stack is not empty and then pop it
    # How to hold each person's stack?
    mis_entries = []
    mis_exits = []
    per_dict = {}
    for rec in records:
        per, state = rec[0], rec[1]
        per_stack = []
        if per in per_dict:
            per_stack = per_dict.get(per)
        else:
            per_dict[per] = per_stack
        if state == 'enter':
            if per_stack == []:
                per_stack.append('enter')
                per_dict[per] = per_stack
            else:
                if per not in mis_entries:
                    mis_entries.append(per);
        else: # exit
            if per_stack == []:
                if per not in mis_exits:
                    mis_exits.append(per);
            else:
                per_stack.pop()
                per_dict[per] = per_stack
                
    for per in per_dict:
        per_stack = per_dict.get(per)
        if per_stack != []:
            item = per_stack.pop()
            if item == 'enter':
                if per not in mis_entries:
                    mis_entries.append(per);
            else:
                if per not in mis_exits:
                    mis_exits.append(per);
    return [mis_entries, mis_exits]

def mismatches_better(records):
    mis_entries = set()
    mis_exits = set()
    per_dict = {}
    for rec in records:
        per, state = rec[0], rec[1]
        if per not in per_dict:
            per_dict[per] = 0
        if state == 'enter':
            per_dict[per] += 1
        else: # exit
            per_dict[per] -= 1
                
    for per, count in per_dict.items():
        if count > 0:
            mis_entries.add(per)
        elif count < 0:
            mis_exits.add(per)
    
    return [list(mis_entries), list(mis_exits)]