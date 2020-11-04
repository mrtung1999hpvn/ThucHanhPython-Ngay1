import random
n = int(input('Nhap n : '))
while n < 0 or n > 99:
  n = int(input('Nhap n : '))
KetQua = [random.randint(1,100) for i in range (n)]
f = open('ketqua.txt', 'w')
_str = ''
for i in range (n): _str += str(KetQua[i]) + ' '
print(_str)
f.write(_str)
f.close()
