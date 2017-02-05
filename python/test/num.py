# coding: utf-8

numbers = [15, 35, 80]

def read_visits(data_path):
    with oepn(data_path) as f:
        for line in f:
            yield int(line)

def nomalize(number):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return resut


it = read_visits('my_numbers.txt')


