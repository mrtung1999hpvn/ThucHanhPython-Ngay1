import operator
class Sach:
    def __init__(self,ten,sotrang,giatien):
      self.ten = ten
      self.sotrang = sotrang
      self.giatien = giatien
print('-----Nhap danh sach sach-----')
n=int(input('Nhap so luong sach : '))
while n < 0 or n >99:
  n = int(input('Nhap so luong sach : '))
ThuVien = [Sach(input('Nhap ten sach : '),input('Nhap so trang : '),input('Nhap gia tien : ')) for i in range (n)]
print('-----Xuat danh sach sach-----')
for i in range (n):
  print(f'{i+1} Ten sach : {ThuVien[i].ten} So Trang : {ThuVien[i].sotrang} Gia Tien : {ThuVien[i].giatien}')
ThuVien = sorted(ThuVien, key=lambda thuvien:thuvien.giatien, reverse=False)
KetQua = ''
print('-----Sap xep danh sach sach-----')
for i in range (n):
  KetQua += f'{i+1} Ten sach : {ThuVien[i].ten} So Trang : {ThuVien[i].sotrang} Gia Tien : {ThuVien[i].giatien}'
  if(i+1!=n):
    KetQua += '\n'
print(KetQua)
print('-----In danh sach sach-----')
f = open('sach.txt', 'w')
f.write(KetQua)
f.close()
print(KetQua)
