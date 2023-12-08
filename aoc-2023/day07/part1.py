from fileinput import input
import itertools
import functools

card_index = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
}


def hand_counts_bid(line):
    hand, bid = line.split(' ')
    counts = [0] * 13
    for card in hand:
        counts[card_index[card]] += 1

    return hand, counts, int(bid)


def hand_type_rank(counts):
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts and 2 in counts:
        return 4
    if 3 in counts:
        return 3
    if sum(1 for x in counts if x == 2) == 2:  # two pair
        return 2
    if 2 in counts:
        return 1
    return 0


def hand_rank(hand, counts, bid):
    return (hand_type_rank(counts), card_index[hand[0]], card_index[hand[1]],
            card_index[hand[2]], card_index[hand[3]], card_index[hand[4]])


sorted_hands_and_bids = sorted((hand_counts_bid(line) for line in input()), key=lambda x: hand_rank(*x))

result = sum((i + 1) * hand_and_bid[2] for i, hand_and_bid in enumerate(sorted_hands_and_bids))

print(result)
