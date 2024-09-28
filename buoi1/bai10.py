class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"Điểm: ({self.x}, {self.y})")

import math

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)  # Gọi hàm khởi tạo của lớp cha
        self.a = a  # Bán trục lớn
        self.b = b  # Bán trục nhỏ

    def dien_tich(self):
        return math.pi * self.a * self.b

    def hien_thi(self):
        super().hien_thi()  # Hiển thị thông tin điểm
        print(f"Bán trục lớn: {self.a}, Bán trục nhỏ: {self.b}")

class DuongTron(Elip):
    def __init__(self, x, y, ban_truc):
        super().__init__(x, y, ban_truc, ban_truc)  # Đường tròn là elip với a = b
        self.ban_truc = ban_truc  # Bán kính

    def dien_tich(self):
        return math.pi * self.ban_truc ** 2

    def hien_thi(self):
        super().hien_thi()  # Hiển thị thông tin elip
        print(f"Bán kính: {self.ban_truc}")

if __name__ == "__main__":
    print("Chương trình quản lý hình học:")
    loai_hinh = input("Nhập loại hình (elip, đường tròn): ").strip().lower()

    if loai_hinh == "elip":
        x = float(input("Nhập tọa độ x của điểm: "))
        y = float(input("Nhập tọa độ y của điểm: "))
        a = float(input("Nhập bán trục lớn: "))
        b = float(input("Nhập bán trục nhỏ: "))
        hinh = Elip(x, y, a, b)

        # Hiển thị thông tin elip
        hinh.hien_thi()
        print(f"Diện tích elip: {hinh.dien_tich()}")

    elif loai_hinh == "đường tròn":
        x = float(input("Nhập tọa độ x của điểm: "))
        y = float(input("Nhập tọa độ y của điểm: "))
        ban_truc = float(input("Nhập bán kính: "))
        hinh = DuongTron(x, y, ban_truc)

        # Hiển thị thông tin đường tròn
        hinh.hien_thi()
        print(f"Diện tích đường tròn: {hinh.dien_tich()}")

    else:
        print("Loại hình không hợp lệ.")
