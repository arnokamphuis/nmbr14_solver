from collections import deque
from copy import deepcopy
from itertools import combinations 

prevs = {}
solutions = []

class State:
    target = 0
    numbers = [0,0,0,0,0,0]
    operations = []

    def save_solution(self):
        global solutions
        solutions = solutions + [self.operations]

    def __init__(self, vals, target, operations):
        self.numbers = vals
        self.numbers.sort()
        self.target = target
        self.operations = operations

    def next_states(self):
        result = set({})
        options = combinations(self.numbers, 2)
        for opt in options:
            nums = deepcopy(self.numbers)
            nums.remove(opt[0])
            nums.remove(opt[1])

            s1 = State(nums + [int(opt[0]+opt[1])], self.target, self.operations + [str(opt[0])+'+'+str(opt[1])])
            if opt[0] - opt[1] > 0:
                s2 = State(nums + [int(opt[0]-opt[1])], self.target, self.operations + [str(opt[0])+'-'+str(opt[1])])
            else:
                s2 = None
            s3 = State(nums + [int(opt[0]*opt[1])], self.target, self.operations + [str(opt[0])+'*'+str(opt[1])])
            if opt[1] != 0 and opt[0]%opt[1] == 0:
                s4 = State(nums + [int(opt[0]/opt[1])], self.target, self.operations + [str(opt[0])+'/'+str(opt[1])])
            else:
                s4 = None
            
            if self.target in s1.numbers:
                s1.save_solution()
            elif len(s1.numbers)>1:
                result = result.union(set({s1}))

            if s2:
                if self.target in s2.numbers:
                    s2.save_solution()
                elif len(s2.numbers)>1:
                    result = result.union(set({s2}))

            if self.target in s3.numbers:
                s3.save_solution()
            elif len(s3.numbers)>1:
                result = result.union(set({s3}))

            if s4:
                if self.target in s4.numbers:
                    s4.save_solution()
                elif len(s4.numbers)>1:
                    result = result.union(set({s4}))

        for r in result:
            prevs[r] = self
        return result


# start = State([1,5,6,2,50,25], 813, [])
start = State([25,3,7,8,6,9], 223, [])

all_states = set({start})

while len(all_states) > 0:
    c_s = list(all_states).pop()
    all_states.remove(c_s)
    next = c_s.next_states()
    all_states = all_states.union(set(next))

for sol in solutions:
    print(len(sol), start.target, sol)
