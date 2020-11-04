f = open('sach.txt', 'r')
str = f.read().split('\n')
n = int(str[0])
str.pop(0)
print (f'So luong sach : {n}')
DanhSach =[]
KetQua = ''
for i in range (int(n)):
  if str[i].split('/')[0] + ' ' + str[i].split('/')[1] +' ' + str[i].split('/')[2] + '' not in DanhSach:
    print(str[i].split('/')[0] + ' ' + str[i].split('/')[1] +' ' + str[i].split('/')[2] + '')
    DanhSach.append(str[i].split('/')[0] + ' ' + str[i].split('/')[1] +' ' + str[i].split('/')[2] + '')
  if int(str[i].split('/')[2])>100000 and int(str[i].split('/')[1])<200:
    KetQua += str[i].split('/')[0] + ' ' + str[i].split('/')[1] +' ' + str[i].split('/')[2] + ''
print('In ketqua.txt')
f = open('ketqua.txt', 'w')
print(KetQua)
f.write(KetQua)
f.close()
