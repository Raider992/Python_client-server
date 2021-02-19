# 1. Каждое из слов «разработка», «сокет», «декоратор» представить
# в строковом формате и проверить тип и содержание соответствующих
# переменных. Затем с помощью онлайн-конвертера преобразовать
# строковые представление в формат Unicode и также проверить тип
# и содержимое переменных.


str1 = 'разработка'
print(str1)
print(type(str1))

# разработка
# <class 'str'>

str1_uni = b"\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0"
r1 = str1_uni.decode()
print(str1_uni)
print(type(str1_uni))
print(r1)

# b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
# <class 'bytes'>
# разработка


str2 = 'сокет'
print(str2)
print(type(str2))

# сокет
# <class 'str'>

str2_uni = b"\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82"
r2 = str2_uni.decode()
print(str2_uni)
print(type(str2_uni))
print(r2)

# b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
# <class 'bytes'>
# сокет


str3 = 'декоратор'
print(str3)
print(type(str3))

# декоратор
# <class 'str'>

str3_uni = b"\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80"
r3 = str3_uni.decode()
print(str3_uni)
print(type(str3_uni))
print(r3)

# b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
# <class 'bytes'>
# декоратор
