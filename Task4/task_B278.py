# Написать функцию sum_of_fractions, которая получает вещественное число и
# возвращает строку - сумму слагаемых числа в виде дробей.
# Между слагаемыми поставить символ +, все отделить пробелами
#
# Примеры:
# sum_of_fractions(1.24) ==> '1 + 2/10 + 4/100'

import traceback


def sum_of_fractions(num):
    n = list(str(num))
    d = n.index('.')
    c = 10

    a = ''.join(str(n[i]) for i in range(d))
    if a == '0':
        a = ''
    for i in range(d + 1, len(n)):
        if n[i] != '0':
            a += f"{'' if a == '' else ' + '}{n[i]}/{c}"
        c *= 10
    return a


# Тесты
try:
    assert sum_of_fractions(1.24) == '1 + 2/10 + 4/100'
    assert sum_of_fractions(7.304) == '7 + 3/10 + 4/1000'
    assert sum_of_fractions(0.04) == '4/100'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
