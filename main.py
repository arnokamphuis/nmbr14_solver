from collections import deque
from copy import deepcopy
from itertools import combinations 

prevs = {}
solutions = []

class State:
    target = 0
    numbers = [0,0,0,0,0,0]
    operation_count = 0

    def save_solution(self, f, s):
        global solutions
        r = []
        r = r + [f.numbers]
        r = r + [s.numbers]
        p = prevs[s]
        while p:
            r = r + [p.numbers]
            if p in prevs:
                p = prevs[p]
            else:
                p = None
        solutions = solutions + [r]

    def __init__(self, vals, target, operation_count):
        self.numbers = vals
        self.numbers.sort()
        self.target = target
        self.operation_count = operation_count

    def next_states(self):
        result = set({})
        options = combinations(self.numbers, 2)
        for opt in options:
            nums = deepcopy(self.numbers)
            nums.remove(opt[0])
            nums.remove(opt[1])

            s1 = State(nums + [int(opt[0]+opt[1])], self.target, self.operation_count + 1)
            s2 = State(nums + [int(opt[0]-opt[1])], self.target, self.operation_count + 1)
            s3 = State(nums + [int(opt[0]*opt[1])], self.target, self.operation_count + 1)
            if opt[1] != 0 and opt[0]%opt[1] == 0:
                s4 = State(nums + [int(opt[0]/opt[1])], self.target, self.operation_count + 1)
            else:
                s4 = None
            
            if len(s1.numbers)==1:
                if s1.numbers[0] == self.target:
                    self.save_solution(s1,self)
            else:
                result = result.union(set({s1}))

            if len(s2.numbers)==1:
                if s2.numbers[0] == self.target:
                    self.save_solution(s2,self)
            else:
                result = result.union(set({s2}))

            if len(s3.numbers)==1:
                if s3.numbers[0] == self.target:
                    self.save_solution(s3,self)
            else:
                result = result.union(set({s3}))

            if s4:
                if len(s4.numbers)==1:
                    if s4.numbers[0] == self.target:
                        self.save_solution(s4,self)
                else:
                    result = result.union(set({s4}))

        for r in result:
            prevs[r] = self
        return result


    

start = State([1,5,6,2,50,25], 813, 0)

all_states = set({start})

while len(all_states) > 0:
    c_s = list(all_states).pop()
    all_states.remove(c_s)
    next = c_s.next_states()
    all_states = all_states.union(set(next))

for s in solutions:
    print(len(s)-1, s)
