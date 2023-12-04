from fileinput import input
import functools
import collections

def parse_card(line):
    left, picks = line.split('|')
    _, winners = left.split(':')
    winners = set(int(x) for x in (y for y in winners.split(' ') if y != ''))
    picks = set(int(x) for x in (y for y in picks.split(' ') if y != ''))
    return (winners, picks)

def num_points(winners, picks):
    return len(winners.intersection(picks))

cards = [None]

for line in input():
    cards.append(parse_card(line))

visits = collections.Counter()

@functools.lru_cache(maxsize=None)
def card_score(i):
    visits[i] += 1
    pts = num_points(*cards[i])
    adjacent = list(i+1+di for di in range(pts) if i+1+di < len(cards))
    return 1 + sum(card_score(c) for c in adjacent)

print(sum(card_score(i) for i in range(1, len(cards))))