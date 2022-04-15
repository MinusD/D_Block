import os
import sys
import glob
import re
import shutil
import subprocess
import time


def create_and_copy():
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Папка, откуда запускаемся
    # print(app_path)
    data_path = os.path.join(app_path, "Ознакомительная папка")
    filenames = glob.glob(os.path.join(app_path, "*.py"))
    theme_a = os.path.join(data_path, "тема A")
    os.makedirs(theme_a, exist_ok=True)
    theme_b = os.path.join(data_path, "тема В")
    os.makedirs(theme_b, exist_ok=True)
    for filename in filenames:
        if os.path.isfile(filename):
            if re.search(r'task_A\d{3}.py', filename):
                shutil.copy2(filename, theme_a)
            elif re.search(r'task_B\d{3}.py', filename):
                shutil.copy2(filename, theme_b)


def parse_folders():
    pattern = r'(def )([a-zA-Z0-9_,\(\)]+):'
    data_path = os.path.realpath('Ознакомительная папка')
    for address, dirs, files in os.walk(data_path):
        if address != data_path:
            if len(files):
                print(f'folder \"{os.path.basename(address)}\"')
                for file in files:
                    if re.search(r'task_\w{4}.py', file):
                        print(f'>>> script \"{file}\"')
                        p = address + "\\" + file
                        text = open(p, 'r', encoding='UTF-8').read()
                        is_set_func = re.search(pattern, text)
                        if is_set_func:
                            for func in re.finditer(pattern, text):
                                print(f'>>> >>> function \"{func.group(2)}\"')
                            time_start = time.time()
                            print(f'>>> >>> output \"{subprocess.getoutput(["python", p])}\"')
                            print(f'>>> >>> time \"{round(time.time() - time_start, 3)} sec\"')

                    # os.startfile(p)
                    # subprocess.run(["py", p])
                    # eval(open(p, 'r', encoding='UTF-8').read())
                # result = eval(open(p, 'r').read())
                # print((open(p, 'r').read()))

    # for filename in sorted(files):
    #   print(" - {} | {:.2f} Кб".format(filename, os.path.getsize(filename)/ 1024))


if __name__ == '__main__':
    create_and_copy()
    parse_folders()
