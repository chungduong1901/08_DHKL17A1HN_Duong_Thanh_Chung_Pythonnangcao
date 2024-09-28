import math
class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kiem_tra_hop_le()
    #kiểm tra tính hợp lệ của phân số
    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0!")
    #nhập phân số
    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        self.kiem_tra_hop_le()
    #in phân số
    def in_phan_so(self):
        if self.mau_so == 1:
            print(f"Phân số: {self.tu_so}")
        else:
            print(f"Phân số: {self.tu_so}/{self.mau_so}")
    #rút gọn phân số
    def rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
if __name__ == "__main__":
    phan_so = PhanSo()
    phan_so.nhap_phan_so()
    phan_so.rut_gon()
    phan_so.in_phan_so()
