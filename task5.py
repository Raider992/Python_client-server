# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый
# тип на кириллице.

import subprocess
import chardet


args = ['ping', '-n', '3', 'yandex.ru']
args2 = ['ping', '-n', '3', 'youtube.com']

subproc_ping1 = subprocess.Popen(args, stdout=subprocess.PIPE)
subproc_ping2 = subprocess.Popen(args2, stdout=subprocess.PIPE)

for line in subproc_ping1.stdout:
    # encoding = chardet.detect(line)
    # print(encoding)
    line2 = line.decode('IBM866', errors='replace')
    print(line2)


for line in subproc_ping2.stdout:
    # encoding = chardet.detect(line)
    # print(encoding)
    line2 = line.decode('IBM866', errors='replace')
    print(line2)
