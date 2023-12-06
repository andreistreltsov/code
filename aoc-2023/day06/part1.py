from fileinput import input
import itertools
import functools

lines = input()
race_times = (int(x) for x in next(lines).split(':')[1].split(' ') if x != '')
race_distances = (int(x) for x in next(lines).split(':')[1].split(' ') if x != '')
races = zip(race_times, race_distances)

def distance(charge_time, race_time):
    return (race_time-charge_time)*charge_time

def num_ways_to_win(race_time, record_distance):
    return sum(1 for charge_time in range(0, race_time+1) 
               if distance(charge_time, race_time) > record_distance)


print(functools.reduce(lambda a,x: a*x, list(num_ways_to_win(*race) for race in races), 1))

