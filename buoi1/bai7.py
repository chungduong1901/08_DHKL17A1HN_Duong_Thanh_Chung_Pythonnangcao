class Date:
    def __init__(self, day=1, month=1, year=2000):
        """Hàm tạo: Khởi tạo ngày, tháng, năm với các giá trị mặc định."""
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin ngày, tháng, năm ra màn hình."""
        print(f"Ngày {self.day}/{self.month}/{self.year}")

    def next(self):
        """Tính ngày tiếp theo."""
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.year % 400 == 0) or (self.year % 100 != 0 and self.year % 4 == 0):
            days_in_month[1] = 29
        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

# Chương trình chính
if __name__ == "__main__":
    date = Date(28, 2, 2020)
    date.display() 
    date.next()
    date.display() 
