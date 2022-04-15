# Написать функцию sequence_classifier(arr), которая возвращает тип последовательности.
#
# тип пояснение пример
# 0 неупорядоченная [3,5,8,1,14,3]
# 1 строго возрастающая [3,5,8,9,14,23]
# 2 неубывающая [3,5,8,8,14,14]
# 3 строго убывающая [14,9,8,5,3,1]
# 4 невозрастающая [14,14,8,8,5,3]
# 5 постоянная [8,8,8,8,8,8]
#
# Пример:
# sequence_classifier([8,9]) ==> 1



import traceback


def sequence_classifier(arr):
    f1 = True
    f2 = True
    f3 = True
    f4 = True
    f5 = True
    for i in range(1, len(arr)):
        f5 = False if arr[i-1] != arr[i] else f5
        f4 = False if arr[i-1] < arr[i] else f4
        f3 = False if arr[i-1] <= arr[i] else f3
        f2 = False if arr[i-1] > arr[i] else f2
        f1 = False if arr[i-1] >= arr[i] else f1
    #print(f1,f2,f3,f4,f5)
    if f1:
        ans = 1
    elif f3:
        ans = 3
    elif f5:
        ans = 5
    elif f2:
        ans = 2
    elif f4:
        ans = 4
    else:
        ans = 0
    return ans


# Тесты
try:
    assert sequence_classifier([3, 5, 8, 1, 14, 3]) == 0
    assert sequence_classifier([3, 5, 8, 9, 14, 23]) == 1
    assert sequence_classifier([3, 5, 8, 8, 14, 14]) == 2
    assert sequence_classifier([14, 9, 8, 5, 3, 1]) == 3
    assert sequence_classifier([14, 14, 8, 8, 5, 3]) == 4
    assert sequence_classifier([8, 8, 8, 8, 8, 8]) == 5
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
