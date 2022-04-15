# Написать функцию count_seven, которая определяет количество вхождений цифры 7 в заданное число
#
# Пример:
# count_seven(171717) ==> 3

import traceback


def count_seven(number):
    counter = 0
    while number != 0:
        if number % 10 == 7:
            counter+=1
        number //= 10
    return counter


# Тесты
try:
    assert count_seven(0) == 0
    assert count_seven(1) == 0
    assert count_seven(7) == 1
    assert count_seven(7777777) == 7
    assert count_seven(304050607) == 1
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
