class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh 1
        self.b = b  # Cạnh 2
        self.c = c  # Cạnh 3

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        # Sử dụng công thức Heron để tính diện tích
        p = self.chu_vi() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def hien_thi(self):
        print(f"Cạnh 1: {self.a}, Cạnh 2: {self.b}, Cạnh 3: {self.c}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        # Với tam giác vuông, a và b là hai cạnh góc vuông
        super().__init__(a, b, (a**2 + b**2) ** 0.5)  # Cạnh huyền được tính từ hai cạnh góc vuông

    def hien_thi(self):
        print("Tam giác vuông:")
        super().hien_thi()

class TamGiacDeu(TamGiacVuong):
    def __init__(self, canh):
        super().__init__(canh, canh)  # Gọi đến hàm khởi tạo của lớp cha

    def hien_thi(self):
        print("Tam giác đều:")
        super().hien_thi()

if __name__ == "__main__":
    print("Chương trình quản lý hình tam giác:")
    loai_hinh = input("Nhập loại hình (tam giác, tam giác vuông, tam giác đều): ").strip().lower()

    if loai_hinh == "tam giác":
        a = float(input("Nhập cạnh 1: "))
        b = float(input("Nhập cạnh 2: "))
        c = float(input("Nhập cạnh 3: "))
        hinh = TamGiac(a, b, c)
    
    elif loai_hinh == "tam giác vuông":
        a = float(input("Nhập cạnh góc vuông 1: "))
        b = float(input("Nhập cạnh góc vuông 2: "))
        hinh = TamGiacVuong(a, b)

    elif loai_hinh == "tam giác đều":
        canh = float(input("Nhập cạnh: "))
        hinh = TamGiacDeu(canh)

    else:
        print("Loại hình không hợp lệ.")
        exit()

    # Hiển thị thông tin hình
    hinh.hien_thi()
