from fileinput import input
import itertools
from collections import defaultdict

lines = list(line.strip() for line in input())
m, n = len(lines), len(lines[0])
GEAR = '*'

def nums_in_line(line):
    digits = []
    for i,c in enumerate(itertools.chain(line, '\n')):
        if c.isdigit():
            digits.append(c)
        elif digits:
            number = int(''.join(d for d in digits))
            start_idx = i-len(digits)
            yield (start_idx, number, len(digits))
            digits.clear()

def nums_in_input():
    for row, line in enumerate(lines): 
        for x in nums_in_line(line):
            col, x, size = x
            yield (row, col, x, size)
    
def adjacent_cells(row,col,size):
    for j in range(col-1, col+size+1): #yield the top row
       yield (row-1, j) 
    yield (row, col-1)                 # yield the mid row
    yield (row, col+size) 
    for j in range(col-1, col+size+1): # yield the bottom row
       yield (row+1, j) 
    
gear_to_adjacent_numbers = defaultdict(list)

for (row,col,x,size) in nums_in_input():
    for r,c in adjacent_cells(row,col,size):
        if 0 <= r < m and 0 <= c < n and lines[r][c] == GEAR:
            gear_to_adjacent_numbers[(r,c)].append(x)

solution = sum(nums[0]*nums[1] for nums in gear_to_adjacent_numbers.values() if len(nums) == 2)

print(solution)
