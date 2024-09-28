class Stack:
    def __init__(self, capacity=10):
        """Hàm tạo: khởi tạo ngăn xếp với dung lượng tối đa."""
        self.capacity = capacity 
        self.stack = []

    def is_empty(self):
        """Kiểm tra ngăn xếp có trống không."""
        return len(self.stack) == 0

    def is_full(self):
        """Kiểm tra ngăn xếp có đầy không."""
        return len(self.stack) == self.capacity

    def push(self, value):
        """Đưa một phần tử vào ngăn xếp."""
        if self.is_full():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.stack.append(value) 
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        """Lấy một phần tử từ đỉnh ngăn xếp."""
        if self.is_empty():
            print("Ngăn xếp trống, không thể lấy phần tử.")
        else:
            value = self.stack.pop()
            print(f"Đã lấy {value} từ ngăn xếp.")
            return value

# Chương trình chính
if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1.2)
    stack.push(2.5)
    stack.push(3.7)
    stack.push(4.8)
    stack.push(5.9)
    stack.push(6.1)
    stack.pop()
    stack.pop()
    print(f"Ngăn xếp rỗng: {stack.is_empty()}")
    print(f"Ngăn xếp đầy: {stack.is_full()}")
