class SinhVien:
    def __init__(self,MaSV,TenSV,LopHocPhan):
        self.MaSV = MaSV
        self.TenSV = TenSV
        self.LopHocPhan = LopHocPhan
    def setSinhVien(self,MaSV,TenSV,LopHocPhan):
        self.MaSV = MaSV
        self.TenSV = TenSV
        self.TenSV = LopHocPhan
    def getSinhVien(self):
        return str(self.MaSV)+"-"+str(self.TenSV)+"-"+str(self.LopHocPhan)
    
        
class ReadData(SinhVien):
    def __init__(self,f):
        self.Data = []
        self.f = open(f, 'r')
    def Open(self,link):
        self.f = open(link, 'r')
    def setDanhSachSinhVien(self,data):
        self.Data = data
    def getDanhSachSinhVien(self):
        return self.Data
    def readAllData(self):
        Data = self.f.read().split('\n')
        self.Data=Data
    def readToSinhVien(mang):
        return [SinhVien(mang[i].split('-')[0],mang[i].split('-')[1],mang[i].split('-')[2]) for i in range(int(len(mang)))]
    def GetData(self):
        return self.Data
    def Close(self):
        self.f.close()
class WriteData(SinhVien):
    def __init__(self,link):
        self.Data = []
        self.f = open(link, 'w')
    def Open(self,link):
        self.f = open(link, 'w')
    def WriteAllData(self,_str):
        self.f.write(_str)
    def Close(self):
        self.f.close()


    
def LuuFileText(_str):
    p2 = WriteData('data.txt')
    p2.WriteAllData(_str)
    p2.Close()
    
def ThemSinhVien():
    print("******************************************")
    print('Thêm sinh viên')
    p1 = ReadData('data.txt')
    p1.Open('data.txt')
    p1.readAllData()
    MangSinhVien = ReadData.readToSinhVien(p1.GetData())
    MaSV,TenSV,LopHocPhan = str(input('Nhập mã sinh viên : ')),str(input('Nhập tên sinh viên : ')),str(input('Nhập lớp học phần : '))
    MangSinhVien.append(SinhVien(MaSV,TenSV,LopHocPhan))
    p1.setDanhSachSinhVien(MangSinhVien)
    kq =''
    for i in range (int(len(p1.getDanhSachSinhVien()))):
        kq += str(p1.getDanhSachSinhVien()[i].MaSV) +"-"+str(p1.getDanhSachSinhVien()[i].TenSV)+"-"+str(p1.getDanhSachSinhVien()[i].LopHocPhan)+"\n"
    LuuFileText(kq[:-1])
    p1.Close()
    print("Thêm thành công")
    

    
def SuaSinhVien():
    print("******************************************")
    print('Sửa sinh viên')
    print('!!! Chú thích : Không sửa trường dữ liệu nào có thể để trống nhấn enter !!!')
    HienThiDanhSachSinhVien()
    MaSV = str(input('Xin vui lòng nhập mã sinh viên cần sửa: '))
    _MaSV,_TenSV,_LopHocPhan = str(input('Sửa mã sinh viên : ')),str(input('Sửa tên sinh viên : ')),str(input('Sửa lớp học phần : '))
    p1 = ReadData('data.txt')
    p1.Open('data.txt')
    p1.readAllData()
    MangSinhVien = ReadData.readToSinhVien(p1.GetData())
    for i in range (int(len(MangSinhVien))-1):
        if MangSinhVien[i].MaSV == str(MaSV):
            if _MaSV!='':
                print('Cập nhập mã sinh viên . . .')
                MangSinhVien[i].MaSV = _MaSV
            if _TenSV!='':
                print('Cập nhập tên sinh viên . . .')
                MangSinhVien[i].TenSV = _TenSV
            if _LopHocPhan!='':
                print('Cập nhập lớp học phần . . .')
                MangSinhVien[i].LopHocPhan = _LopHocPhan
    kq =''
    for i in range (int(len(MangSinhVien))):
        kq += str(MangSinhVien[i].MaSV) +"-"+str(MangSinhVien[i].TenSV)+"-"+str(MangSinhVien[i].LopHocPhan)+"\n"
    LuuFileText(kq[:-1])
    p1.Close()
    HienThiDanhSachSinhVien()
    
def XoaSinhVien():
    print("******************************************")
    HienThiDanhSachSinhVien()
    print('Xoá sinh viên')
    MaSV = str(input('Xin vui lòng nhập mã sinh viên : '))
    p1 = ReadData('data.txt')
    p1.Open('data.txt')
    p1.readAllData()
    MangSinhVien = ReadData.readToSinhVien(p1.GetData())
    for i in range (int(len(MangSinhVien))-1):
        if MangSinhVien[i].MaSV == MaSV:
            print(MangSinhVien[i].MaSV == MaSV)
            del MangSinhVien[i]
            print("Xoá thành công")
    kq =''
    for i in range (int(len(MangSinhVien))-1):
        kq += str(MangSinhVien[i].MaSV) +"-"+str(MangSinhVien[i].TenSV)+"-"+str(MangSinhVien[i].LopHocPhan)+"\n"

    LuuFileText(kq[:-1])
    p1.Close()
    
def TimKiemSinhVienTheoMa():
    print("******************************************")
    print('Tìm kiếm sinh viên theo mã')
    p1 = ReadData('data.txt')
    p1.Open('data.txt')
    p1.readAllData()
    MangSinhVien = ReadData.readToSinhVien(p1.GetData())
    MaSV = str(input('Xin vui lòng nhập mã sinh viên : '))
    for i in range (int(len(MangSinhVien))):
        if MangSinhVien[i].MaSV == MaSV:
            print('Tìm thành công')
            print(str(MangSinhVien[i].MaSV) + "-" + str(MangSinhVien[i].TenSV) + "-"+str(MangSinhVien[i].LopHocPhan))
            
def HienThiDanhSachSinhVien():
    print("******************************************")
    print('Hiển thị danh sách sinh viên')
    p1 = ReadData('data.txt')
    p1.Open('data.txt')
    p1.readAllData()
    MangSinhVien = ReadData.readToSinhVien(p1.GetData())
    print('MSV - Tên sinh viên - Lớp học phần')
    for i in range (int(len(MangSinhVien))):
       print(str(MangSinhVien[i].MaSV) + "-" + str(MangSinhVien[i].TenSV) + "-"+str(MangSinhVien[i].LopHocPhan))
    p1.Close()
def Menu(x):
    p1 = ReadData('data.txt')
    if(int(x)==1):
        ThemSinhVien()
    if(int(x)==2):
        SuaSinhVien()
    if(int(x)==3):
        XoaSinhVien()
    if(int(x)==4):
        HienThiDanhSachSinhVien()
    if(int(x)==5):
        TimKiemSinhVienTheoMa()

def __main__():
    #try:
        while(True):
            print("******************************************")
            print("*     0. Thoát chương trình              *")
            print("*     1. Thêm sinh viên                  *")
            print("*     2. Sửa danh sách sinh viên         *")
            print("*     3. Xoá danh sách sinh viên         *")
            print("*     4. Hiển thi danh sách sinh viên    *")
            print("*     5. Tìm kiếm sinh viên theo mã      *")
            print("******************************************")
            n= int(input('Xin vui lòng chọn !'))
            if(n==0):
                _exit = str(input('Bạn muốn thoát chương trình ? (1 - Có , 2 - Không)'))
                if _exit=='1':
                    break
                else:
                    __main__()
            else:
                Menu(n)
    #except:
        #print("Lỗi hệ thống xin vui lòng đóng chương trình khởi động lại . . .")


__main__()
    
    

