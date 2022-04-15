import re


def repl(t):
    return str(int(int(t.group()[:-5]) / 3.6)) + " м/с"


if __name__ == '__main__':
    data = input()
    # data = "Шакал разгоняется до скорости 72 км/ч, а гепард до 108 км/ч."
    pattern = r'(\d+) км/ч'
    '''pattern4 = r'[0-9]+ км/ч)'
    pattern3 = r'([0-9]+ км/ч)'
    pattern2 = r'(\d+ км/ч)'
    repl2 = r'\1/3.6 м/с'
    repl1 = r'\n м/с'
    '''
    print(re.sub(pattern, repl, data))
