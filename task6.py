# 6. Создать текстовый файл test_file.txt, заполнить его
# тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести
# его содержимое.


# Так как у меня windows

import locale
locale.getpreferredencoding()

# Выдаёт:
# 'cp1251'


import chardet
import io

with open('test_file.txt', 'rb') as f:
    bts = f.read()
    print(chardet.detect(bts))


# chardet выдаёт такой результат:
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# Но в то же время, если просто набрать в консоли код:

f = open('test_file.txt', 'r')
print(f)

# Выдаёт вот это:
# <_io.TextIOWrapper name='test_file.txt' mode='r' encoding='cp1251'>

# Предполагаю, здесь имеет место совпадение кодов символов, потому что
# файл создавался в windows и, по идее, должен иметь дефолтную
# кодировку для кириллицы cp1251.


with io.open('test_file.txt', 'rb') as f:
    cnt = f.read()
    print(cnt)

# Выводит:
# b'\xd1\x81\xd0\xb5\xd1\x82\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\r\n\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82\r\n\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
