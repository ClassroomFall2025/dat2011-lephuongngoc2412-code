class SanPham:
    def __init__(self):
        self.ten_san_pham = ""
        self.gia = ""
        self.giam_gia = ""
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def nhap_sp(self):
        self.ten_san_pham = input("Tên sản phẩm:")
        self.gia = float(input("Giá:"))
        self.giam_gia = float(input("Giảm giá:"))
    def xuat_thong_tin_sp(self):
        print(f"Sản phẩm {self.ten_san_pham} có giá {self.gia} và được giảm giá {self.giam_gia}")
        





