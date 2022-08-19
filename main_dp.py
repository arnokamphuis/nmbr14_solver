from collections import deque
from copy import deepcopy
from itertools import combinations 
from collections import defaultdict

prevs = {}
solutions = []
DP = {}

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

    def solve(self):
        global DP
        if str(self.operations) in DP:
            return
        ls, ns = self.next_states()

        if len(ls) > 0:
            for s in ls:
                s.save_solution()
            DP[str(self.operations)] = ls
        for s in ns:
            s.solve()

    def next_states(self):
        result = set({})
        local_solutions = set({})
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
                local_solutions = local_solutions.union(set({s1}))
            elif len(s1.numbers)>1:
                result = result.union(set({s1}))

            if s2:
                if self.target in s2.numbers:
                    local_solutions = local_solutions.union(set({s2}))
                elif len(s2.numbers)>1:
                    result = result.union(set({s2}))

            if self.target in s3.numbers:
                local_solutions = local_solutions.union(set({s3}))
            elif len(s3.numbers)>1:
                result = result.union(set({s3}))

            if s4:
                if self.target in s4.numbers:
                    local_solutions = local_solutions.union(set({s4}))
                elif len(s4.numbers)>1:
                    result = result.union(set({s4}))

        for r in result:
            prevs[r] = self
        return local_solutions, result


old = [
    State([1,5,6,2,50,25], 813, []),
    State([25,3,7,8,6,9], 223, []),
    State([4,7,2,9,100,50], 997, []),
    State([6,8,2,50,8,8], 607, []),
    State([2,4,50,6,6,8], 509, []),
    State([50,4,50,6,6,8], 661, []),
    State([1,3,6,2,25,10], 984, []),
    State([6,2,6,7,25,50], 566, []),
    State([5,7,2,8,10,100], 942, []),
    State([5,7,2,8,75,100], 942, []),
    State([1,3,3,6,7,25], 254, []),
    State([1,3,3,7,10,50], 513, []),
    State([2,6,6,8,10,25], 412, []),
    State([1,3,25,8,9,25], 607, []),
    State([2,9,7,10,7,25], 473, []),
    State([8,8,9,3,25,75], 723, []),
    State([1,3,8,9,9,25], 601, []),
    State([5,2,3,8,10,75], 872, []),
    State([7,6,4,8,10,25], 419, []),
    State([9,6,7,8,3,100], 255, []),
    State([4,8,7,7,25,25], 579, []),
    State([2,5,3,9,50,25], 479, []),
    State([6,9,9,8,5,3], 275, []),
    State([9,2,7,6,50,25], 702, []),
    State([1,7,8,9,1,75], 654, []),
    State([10,2,5,3,7,10], 234, []),
    State([9,6,10,3,8,100], 528, []),
    State([6,6,2,8,50,75], 901, []),
    State([1,2,6,7,50,3], 323, []),
    State([9,7,4,8,25,50], 850, []),
    State([9,9,10,4,8,100], 543, []),
    State([8,8,8,8,8,8], 264, []),
    State([6,1,2,3,50,8], 476, []),
    State([1,3,10,6,8,25], 818, []),
    State([4,3,6,5,7,8], 612, []),
    State([2,3,9,3,50,7], 722, []),
    State([3,3,8,7,7,8], 394, []),
    State([2,3,25,8,7,75], 911, []),
    State([3,6,5,10,2,2], 161, []),
    State([9,8,2,3,6,10], 523, []),
    State([3,8,8,9,9,10], 526, []),
    State([5,8,4,2,3,8], 181, []),
    State([7,2,3,75,4,50], 458, []),
    State([2,6,7,9,25,25], 804, []),
    State([6,6,7,50,10,1], 298, []),
    State([3,2,9,10,9,25], 782, []),
    State([75,1,4,7,8,25], 322, []),
    State([2,8,3,100,3,50], 651, []),
    State([3,25,6,2,8,100], 933, []),
    State([3,3,25,4,9,10], 538, []),
    State([4,3,9,7,25,75], 378, []),
    State([4,9,7,6,6,50], 118, []),
    State([3,8,100,2,2,6], 654, []),
    State([4,4,5,5,6,100], 962, []),
    State([10,4,4,3,8,10], 272, []),
    State([5,8,25,25,6,6], 468, []),
    State([9,6,2,8,75,50], 842, []),
    State([6,1,9,7,9,10], 183, []),
    State([5,7,7,8,25,10], 463, []),
    State([8,3,7,50,7,50], 730, []),
    State([1,4,25,10,7,8], 393, []),
    State([25,6,6,6,6,50], 626, []),
    State([2,3,2,100,3,4], 501, []),
    State([6,6,6,9,9,100], 206, []),
    State([25,9,8,6,3,1], 970, []),
    State([2,1,3,3,7,9], 111, []),
    State([5,1,4,3,2,10], 191, []),
    State([75,6,1,2,8,75], 712, []),
    State([4,10,5,8,8,10], 807, []),
    State([50,9,3,7,7,5], 509, []),
    State([3,6,9,9,25,100], 721, []),
    State([4,2,3,6,3,3], 227, []),
    State([5,2,4,7,7,6], 411, []),
]

# set the start state to the last one in the old list
start = old[-1]

# solve from the start state using Dynamic Programming
start.solve()

# count and print all the solutions
counts = defaultdict(int)
for sol in solutions:
    counts[len(sol)] = counts[len(sol)] + 1
    print(len(sol), start.target, sol)

# print the counts for the different calculation steps
print("== COUNTS ==")
for k,v in counts.items():
    print(k,v)