from fileinput import input

RED, GREEN, BLUE = 'red', 'green', 'blue'
color_idx = {RED:0, GREEN:1, BLUE:2}
max_cubes = {RED:12, GREEN:13, BLUE:14}

# a game is impossible if it contains a round where the number of cubes of some color is greater than the maximum number of cubes of that color

def parse_game(line):
    """
    For each game returns a tuple like (game_id, [(r1,g1,b1), (r2,g2,b2), ...])
    """
    game, rounds = line.split(':')
    game = int(game.split(' ')[1])
    rounds = rounds.split(';')

    rounds_parsed = []

    for round in rounds:
        round_parsed = [0]*3
        for num_color_pair in [x.strip() for x in round.split(',')]:
            count, color = num_color_pair.split(' ')
            round_parsed[color_idx[color]] = int(count)
        
        rounds_parsed.append(tuple(round_parsed))

    return (game, rounds_parsed)

def required_cubes(game):
    """
    Given a parsed game, return the game id and how many cubes of each color it requires
    """
    return (game[0], (max(x[0] for x in game[1]), 
            max(x[1] for x in game[1]),
            max(x[2] for x in game[1])))

def is_possible(game):
    _, (r, g, b) = game
    return r <= max_cubes[RED] and g <= max_cubes[GREEN] and b <= max_cubes[BLUE]

solution = sum(game[0] for game in (required_cubes(parse_game(line)) for line in input()) if is_possible(game))

print(solution)