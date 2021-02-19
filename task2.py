# 2. Каждое из слов «class», «function», «method» записать
# в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить
# тип, содержимое и длину соответствующих переменных.

c = b"class"
print(c)
print(type(c))
print(len(c))

# b'class'
# <class 'bytes'>
# 5


f = b'function'
print(f)
print(type(f))
print(len(f))

# b'function'
# <class 'bytes'>
# 8


c = b'class'
print(c)
print(type(c))
print(len(c))

# b'class'
# <class 'bytes'>
# 5


# Так как заданные слова написаны латиницей, коды которой присутствуют в ASCII-таблице,
# то содержание и длина переменных будут совпадать, хотя их тип будет байтовый
