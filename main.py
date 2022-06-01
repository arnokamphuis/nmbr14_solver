from collections import deque
from copy import deepcopy
from itertools import combinations 
from collections import defaultdict

prevs = {}
solutions = []

class State:
    target = 0
    numbers = [0,0,0,0,0,0]
    operations = []

    def save_solution(self):
        global solutions
        if self.operations not in solutions:
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

            opt0 = max(opt[0], opt[1])
            opt1 = min(opt[0], opt[1])

            s1 = State(nums + [int(opt0+opt1)], self.target, self.operations + [str(opt0)+'+'+str(opt1)])
            if opt0 != opt1:
                s2 = State(nums + [int(opt0-opt1)], self.target, self.operations + [str(opt0)+'-'+str(opt1)])
            else:
                s2 = None
            s3 = State(nums + [int(opt0*opt1)], self.target, self.operations + [str(opt0)+'*'+str(opt1)])
            if opt1 != 0 and opt0%opt1 == 0:
                s4 = State(nums + [int(opt0/opt1)], self.target, self.operations + [str(opt0)+'/'+str(opt1)])
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
# start = State([25,3,7,8,6,9], 223, [])
# start = State([4,7,2,9,100,50], 997, [])
# start = State([6,8,2,50,8,8], 607, [])
# start = State([2,4,50,6,6,8], 509, [])
# start = State([50,4,50,6,6,8], 661, [])
# start = State([1,3,6,2,25,10], 984, [])
# start = State([6,2,6,7,25,50], 566, [])
# start = State([5,7,2,8,10,100], 942, [])
# start = State([5,7,2,8,75,100], 942, [])
# start = State([1,3,3,6,7,25], 254, [])
# start = State([1,3,3,7,10,50], 513, [])
# start = State([2,6,6,8,10,25], 412, [])
# start = State([1,3,25,8,9,25], 607, [])
# start = State([2,9,7,10,7,25], 473, [])
# start = State([8,8,9,3,25,75], 723, [])
# start = State([1,3,8,9,9,25], 601, [])
start = State([5,2,3,8,10,75], 872, [])

all_states = set({start})

while len(all_states) > 0:
    c_s = list(all_states).pop()
    all_states.remove(c_s)
    next = c_s.next_states()
    all_states = all_states.union(set(next))

counts = defaultdict(int)
for sol in solutions:
    counts[len(sol)] = counts[len(sol)] + 1
    print(len(sol), start.target, sol)

print("== COUNTS ==")
for k,v in counts.items():
    print(k,v)