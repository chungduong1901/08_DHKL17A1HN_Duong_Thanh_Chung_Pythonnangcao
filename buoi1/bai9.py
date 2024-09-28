class DaGiac:
    def __init__(self, ten):
        self.ten = ten

    def dien_tich(self):
        raise NotImplementedError("Phương thức dien_tich() chưa được định nghĩa!")

    def chu_vi(self):
        raise NotImplementedError("Phương thức chu_vi() chưa được định nghĩa!")

    def hien_thi(self):
        print(f"Thông tin {self.ten}:")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")

class HinhBinhHanh(DaGiac):
    def __init__(self, day, chieu_cao):
        super().__init__("Hình bình hành")
        self.day = day
        self.chieu_cao = chieu_cao

    def dien_tich(self):
        return self.day * self.chieu_cao

    def chu_vi(self):
        return 2 * (self.day + self.chieu_cao)

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, rong, cao):
        super().__init__(rong, cao)
        self.rong = rong

    def dien_tich(self):
        return self.rong * self.chieu_cao

    def chu_vi(self):
        return 2 * (self.rong + self.chieu_cao)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def dien_tich(self):
        return self.canh ** 2

    def chu_vi(self):
        return 4 * self.canh

if __name__ == "__main__":
    print("Chương trình quản lý hình học:")
    loai_hinh = input("Nhập loại hình (hình bình hành, hình chữ nhật, hình vuông): ").strip().lower()

    if loai_hinh == "hình bình hành":
        day = float(input("Nhập đáy: "))
        chieu_cao = float(input("Nhập chiều cao: "))
        hinh = HinhBinhHanh(day, chieu_cao)
    
    elif loai_hinh == "hình chữ nhật":
        rong = float(input("Nhập chiều rộng: "))
        cao = float(input("Nhập chiều cao: "))
        hinh = HinhChuNhat(rong, cao)

    elif loai_hinh == "hình vuông":
        canh = float(input("Nhập cạnh: "))
        hinh = HinhVuong(canh)

    else:
        print("Loại hình không hợp lệ.")
        exit()

    # Hiển thị thông tin hình
    hinh.hien_thi()
