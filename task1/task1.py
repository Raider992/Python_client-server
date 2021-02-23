# Решил мейн дату вывести и заполнить отдельно, потому что с моей точки зрения,
# это больше похоже на входные данные(если рассматривать этот скрипт как модуль),
# и если писать в неё внутри функции, надо будет каким-то образом налаживать
# соответствие между элементами списка мейн дата и списками, куда предстоит
# выводить отдельные списки элементов.

import csv
from re import sub

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']

main_data = ['Название ОС', 'Код продукта', 'Тип системы', 'Изготовитель системы']
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []


def process_line(text, line):
    cut_line = sub(rf'^({text})\s+', '', line)
    cut_line = sub(r'\n', '', cut_line)
    return cut_line


def get_data(file_lst):
    os_prod_list.clear()
    os_name_list.clear()
    os_code_list.clear()
    os_type_list.clear()
    for file in file_lst:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('Название ОС:'):
                    cut_line = process_line('Название ОС:', line)
                    os_name_list.append(cut_line)
                if line.startswith('Код продукта:'):
                    cut_line = process_line('Код продукта:', line)
                    os_code_list.append(cut_line)
                if line.startswith('Тип системы:'):
                    cut_line = process_line('Тип системы:', line)
                    os_type_list.append(cut_line)
                if line.startswith('Изготовитель системы:'):
                    cut_line = process_line('Изготовитель системы:', line)
                    os_prod_list.append(cut_line)


def write_to_csv(filename):
    get_data(files)

    data = []
    if len(os_prod_list) == len(os_name_list) == len(os_type_list) == len(os_code_list):
        for i in range(3):
            field = {
                main_data[0]: os_name_list[i],
                main_data[1]: os_code_list[i],
                main_data[2]: os_type_list[i],
                main_data[3]: os_prod_list[i]
            }
            data.append(field)

        with open(filename, 'w', encoding='utf-8') as f:
            f_n_writer = csv.DictWriter(f, fieldnames=main_data, quoting=csv.QUOTE_NONE)
            f_n_writer.writeheader()
            for d in data:
                f_n_writer.writerow(d)


write_to_csv('res.csv')
