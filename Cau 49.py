import random
KetQua=''
f = open('mang.txt', 'r')
So = f.read().split('\n')
n = int(So[0])
Mang = [int(So[1].split(' ')[i]) for i in range (len(So[1].split(' ')))]
print(Mang)
Mang = sorted(Mang,reverse=True)
for i in range (n):
  KetQua += str(Mang[i]) + ' '
print('-----In danh sach sach-----')
f = open('ketqua.txt', 'w')
f.write(KetQua)
f.close()
print(KetQua)
