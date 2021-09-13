import glob
import re


if __name__ == '__main__':
    pattern = r"VALUES \((\d+),"
    pattern_re = re.compile(pattern)

    paths = glob.glob("*.sql")

    for path in paths:
        data = []
        with open(path) as f:
            for line in f:
                index = int(pattern_re.search(line).groups()[0])
                data.append([index, line])

        data.sort(key=lambda x: x[0])

        with open(path, 'w') as f:
            for i, line in data:
                f.write(line)
