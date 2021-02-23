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


def get_data(files):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in files:
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
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)
    # print(os_prod_list)



def write_to_csv(file):
    get_data(files)
    data = []
    if len(os_prod_list) == len(os_name_list) == len(os_type_list) == len(os_code_list):
        for i in range(3):


        with open(file, 'r') as f:
            pass
