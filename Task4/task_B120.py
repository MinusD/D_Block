# Написать функцию reverse_and_combine, которая получает на вход строку, состоящую из строк,
# разделенных пробелами, а затем выполняет следующее:
# 1) если в строке больше одного слова, переверните каждое слово наоборот,
# а затем объедините первое со вторым, третье слово с четвертым, ... (если слов нечетное количество,
# то последнее переворачивается, но не объединяется с другим словом)
# 2) повторять пункт 1, пока слов больше одного, затем вернуть результат (одно слово)
#
# Примеры:
# reverse_and_combine("ab", "cd", "ef") ==> "cdabef"
# 1. "ba"+"dc + " " + "fe" = "badc fe"
# 2. "cdab"+"ef" = "cdabef"

import traceback


def reverse_and_combine(s):
    # Тело функции
    st = ""
    arr = s.split()
    #print(arr)
    if len(arr) > 1:
        for i in range(0, len(arr)-1, 2):
            st += (arr[i][::-1]) + (arr[i+1][::-1]) + " "
            #print(i, st)
        if len(arr)%2:
            st += arr[len(arr)-1][::-1]
    else:
        return arr[0]
    return reverse_and_combine(st)


# Тесты
try:
    assert reverse_and_combine("abc def ghi jkl") == "defabcjklghi"
    assert reverse_and_combine("abc def") == "cbafed"
    assert reverse_and_combine("dfghrtcbafed") == "dfghrtcbafed"
    assert reverse_and_combine("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") == "trzwqfdstrteettr45hh4325543544hjhjh21lllll"
    assert reverse_and_combine("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
