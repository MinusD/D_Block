# Задан список целых чисел. Написать функцию max_three_sum,
# которая возвращает максимальную сумму трех элементов без их повторов
#
# Пример:
# [1,8,3,4,0,8,4] => 15 -> 8 + 4 + 3 = 15


import traceback


def max_three_sum(arr):
    s = set(arr)
    m1 = max(s)
    s.remove(m1)
    m2 = max(s)
    s.remove(m2)
    m3 = max(s)
    return m1 + m2 + m3


# Тесты
try:
    assert max_three_sum([2,1,8,0,6,4,8,6,2,4]) == 18
    assert max_three_sum([-13,-50,57,13,67,-13,57,108,67]) == 232
    assert max_three_sum([-2,-4,0,-9,2]) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
