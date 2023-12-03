from fileinput import input
import itertools

lines = list(line.strip() for line in input())
m, n = len(lines), len(lines[0])

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
    """
    ..... top row
    .123. mid row
    ..... bottom row
    """ 
    for j in range(col-1, col+size+1): #yield the top row
       yield (row-1, j) 
    yield (row, col-1) # yield the mid row
    yield (row, col+size) 
    for j in range(col-1, col+size+1): # yield the bottom row
       yield (row+1, j) 
    
def is_symbol_at(r,c):
    x = lines[r][c]
    return not x.isnumeric() and not x == '.'

def is_part_number(row,col,size):
    return any(is_symbol_at(r,c) for (r,c) in adjacent_cells(row,col,size) if 0 <= r < m and 0 <= c < n)

solution = sum(x for (r,c,x,s) in nums_in_input() if is_part_number(r,c,s))

print(solution)