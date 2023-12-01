from fileinput import input

first_digit = lambda line: next(c for c in line if c.isdigit())

print(sum(int(f"{first_digit(line)}{first_digit(reversed(line))}") for line in input()))
