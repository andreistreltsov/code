from fileinput import input

card_index = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
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


def hand_type_rank_wildcard(counts):
    num_wildcards = counts[0]
    counts[0] = 0

    if not num_wildcards:
        return hand_type_rank(counts)

    best_rank = 0
    for augmented_card_index in range(1, len(counts)):
        counts[augmented_card_index] += num_wildcards
        best_rank = max(best_rank, hand_type_rank(counts))
        counts[augmented_card_index] -= num_wildcards

    return best_rank


def hand_rank(hand, counts, bid):
    return (hand_type_rank_wildcard(counts), card_index[hand[0]], card_index[hand[1]],
            card_index[hand[2]], card_index[hand[3]], card_index[hand[4]])


sorted_hands_and_bids = sorted((hand_counts_bid(line) for line in input()), key=lambda x: hand_rank(*x))

result = sum((i + 1) * hand_and_bid[2] for i, hand_and_bid in enumerate(sorted_hands_and_bids))

print(result)