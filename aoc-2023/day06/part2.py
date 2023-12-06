from fileinput import input
from math import sqrt, floor, ceil

lines = input()
race_time = int(next(lines).replace(' ','').split(':')[1])
race_distance = int(next(lines).replace(' ','').split(':')[1])

def num_ways_to_win(race_time, record_distance):
    """
    A constant-time way to compute the number of ways to win by solving a quadratic
    equation for the charging time c.
    """
    r, t = race_time, record_distance
    d = r**2 - 4*t
    c1, c2 = ceil((r - sqrt(d))/2), floor((r + sqrt(d))/2)
    return c2-c1+1
 
print(num_ways_to_win(race_time, race_distance))
