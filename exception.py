import sys

data = [line.strip() for line in sys.stdin]

for c in data:
    if len(c) < 9:
        print('LengthError')
        continue
    if c.lower() == c or c.upper() == c:
        print('LetterError')
        continue
    if c.isalpha():
        print('DigitError')
        continue
    else:
        print('Success!')
        break
