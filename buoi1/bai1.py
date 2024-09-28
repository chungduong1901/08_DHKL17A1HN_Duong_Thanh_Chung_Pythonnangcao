class HinhChuNhat:
    def __init__(self, chieu_dai=0, chieu_rong=0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    #tính chu vi
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    #tính diện tích
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    #in thông tin hình chữ nhật
    def in_thong_tin(self):
        print(f"Chiều dài: {self.chieu_dai}")
        print(f"Chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")


# Chương trình chính
    # Tạo một đối tượng hình chữ nhật
hinh_chu_nhat = HinhChuNhat()

    # Nhập dữ liệu cho hình chữ nhật
hinh_chu_nhat.nhap_du_lieu()

    # In thông tin hình chữ nhật
hinh_chu_nhat.in_thong_tin()
