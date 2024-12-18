from pathlib import Path
import requests

with open('sessioncookie.txt') as f:
    SESSION_COOKIE = f.read().strip()


def get_input(day, as_list=True):
    input_dir = Path('./input')
    input_dir.mkdir(exist_ok=True)

    filepath = input_dir / f'{day}.txt'

    if not filepath.is_file():
        print(f'Fetching input file for day {day} from AdventOfCode.com...')
        response = requests.get(f'https://adventofcode.com/2024/day/{day}/input',
                                cookies={'session': SESSION_COOKIE})
        if response.ok:
            with open(filepath, 'w') as ipt_file:
                ipt_file.write(response.text)
        else:
            raise ValueError(response.text)

    with open(filepath) as f:
        if as_list:
            return f.read().splitlines()
        else:
            return f.read().strip()
