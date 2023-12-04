from fileinput import input

def parse_card(line):
    left, picks = line.split('|')
    _, winners = left.split(':')
    winners = set(int(x) for x in (y for y in winners.split(' ') if y != ''))
    picks = set(int(x) for x in (y for y in picks.split(' ') if y != ''))
    return (winners, picks)

def num_points(winners, picks):
    num_matches = len(winners.intersection(picks))
    return 0 if not num_matches else 2**(num_matches-1)

solution = sum(num_points(*parse_card(card)) for card in input())

print(solution)