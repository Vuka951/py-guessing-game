import sys
import random

the_num = random.randint(0, 10)

try:
    if len(sys.argv) == 3:
        range_start = int(sys.argv[1])
        range_end = int(sys.argv[2])
        print(list(sys.argv))
        the_num = random.randint(range_start, range_end)
except ValueError:
    print('guess range params invalid(default 0 to 10 will be used)')

while True:
    try:
        current_guess = int(input('Guess a Number: '))
        if the_num == current_guess:
            print(f'Correct the number is {the_num}')
            break
        print('Try Again!')
    except ValueError:
        print('Thats not a number')
