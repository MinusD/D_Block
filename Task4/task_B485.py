"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""


def wiki_function():
    try:
        with open('wiki.txt') as f:
            text = ' '.join(list(filter(lambda s: s != '', (''.join(filter(lambda s: s.isalpha() or s.isspace(),
                                                                           '\n'.join([line.strip() for line in f])))).split(
                '\n'))))
            words_arr = text.split(' ')
            words = set(words_arr)
            wc = dict()
            for a in words:
                wc.update({a: 0})
            for a in words_arr:
                wc.update({a: wc.get(a) + 1})
            wc.pop('')
            wc_sorted = sorted(wc.items(), key=lambda x: x[1], reverse=True)
            top_words = []
            for i in range(10):
                print(f' {i + 1} place --- {wc_sorted[i][0]} --- {wc_sorted[i][1]} times ')
                top_words.append(wc_sorted[i][0])
            for i in range(len(words_arr)):
                if words_arr[i] in top_words:
                    words_arr[i] = 'PYTHON'
            f2 = open('new_wiki.txt', 'w')
            current_line = 0
            for i in range(len(words_arr)):
                if current_line + len(words_arr[i]) > 100:
                    f2.write('\n')
                    current_line = len(words_arr[i])
                else:
                    current_line += len(words_arr[i])
                f2.write(words_arr[i] + " ")
                current_line += 1
        return 1
    except:
        print("File not found")


# Вызов функции
wiki_function()
