import hashlib


def my_generator(filename):
    with open(filename) as f:
        data = f.readlines()
    line_number = 0
    while line_number < len(data):
        yield hashlib.md5(data[line_number].encode('utf-8')).hexdigest()
        line_number += 1


if __name__ == '__main__':
    for item in my_generator('links.txt'):
        print(item)