import re


def repl(t):
    return str(int(int(t.group()[:-5]) / 3.6)) + " м/с"


def km_to_m(s):
    return re.sub(r'(\d+) км/ч', repl, s)


if __name__ == '__main__':
    data = input()
    print(re.sub(r'(\d+) км/ч', repl, data))
    print(km_to_m(data))
