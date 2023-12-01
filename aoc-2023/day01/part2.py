from fileinput import input

substring_to_digit = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

first_digit_in_line = (lambda line, forward: 
                            next(digit for digit in (
                                                substring_to_digit.get(line[i]) or 
                                                substring_to_digit.get(line[i:i+3]) or 
                                                substring_to_digit.get(line[i:i+4]) or 
                                                substring_to_digit.get(line[i:i+5])
                                                for i in (range(len(line)) if forward else reversed(range(len(line))))
                                            ) if digit
                            )
                      )

print(sum(int(f"{d1}{d2}") for d1, d2 in ((first_digit_in_line(line, forward=True), first_digit_in_line(line, forward=False)) for line in input())))
