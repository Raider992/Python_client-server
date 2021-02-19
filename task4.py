# 4. Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя
# методы encode и decode).

str1 = 'разработка'
str1_b = str1.encode()
print(str1_b)
print(str1_b.decode())

# b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
# администрирование


str2 = 'администрирование'
str2_b = str2.encode()
print(str2_b)
print(str2_b.decode())

# b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
# разработка


str3 = 'protocol'
str3_b = str3.encode()
print(str3_b)
print(str3_b.decode())

# b'protocol'
# protocol


str4 = 'standard'
str4_b = str4.encode()
print(str4_b)
print(str4_b.decode())

# b'standard'
# standard

