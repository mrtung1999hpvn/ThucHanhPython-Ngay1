class PhanSo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def setPhanSo(self,a,b):
        self.a = a
        self.b = b
    def getPhanSo(self):
        return str(self.a)+"/"+str(self.b)
    def KiemTraDauVao(self,a,b):
        if(b==0):
            return "Bạn nhập mẫu số bằng 0"
        else:
            return "True"
    def UCLN(a,b):
        if(a%b!=0):
            return PhanSo.UCLN(b,a%b)
        else:
            return b
    def RutGonPhanSo(self):
        ucln = PhanSo.UCLN(self.a,self.b)
        t = self.a/ucln
        m = self.b/ucln
        if m!=1:
            if(m<0):
                m=m*-1
                t=t*-1
            return str(t)+"/"+str(m)
        else:
            return str(t)

p1 = PhanSo(0,0)
try:
    a,b = int(input('Nhập tử số : ')),int(input('Nhập mẫu số : '))
    if(p1.KiemTraDauVao(a,b)=="True"):
        p1.setPhanSo(a,b)
        print("Rút gọn phân số : "+p1.RutGonPhanSo())
    else:
        print(p1.KiemTraDauVao(a,b))
except:
  print("Bạn nhập tử số hoặc mẫu số là số thập phân")

