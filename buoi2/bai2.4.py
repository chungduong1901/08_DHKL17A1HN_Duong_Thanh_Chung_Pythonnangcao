from xml.dom import minidom
doc = minidom.parse('sample.xml')
ten_cong_ty = doc.getElementsByTagName('name')[0].firstChild.data
print("Tên công ty:", ten_cong_ty)

danh_sach_nhan_vien = doc.getElementsByTagName('staff')
for nhan_vien in danh_sach_nhan_vien:
    ma_nhan_vien = nhan_vien.getAttribute('id')  # Lấy thuộc tính id của nhân viên
    ten = nhan_vien.getElementsByTagName('name')[0].firstChild.data  # Tên nhân viên
    luong = nhan_vien.getElementsByTagName('salary')[0].firstChild.data  # Lương nhân viên
    
    print(f"Mã nhân viên: {ma_nhan_vien}")
    print(f"Tên: {ten}")
    print(f"Lương: {luong}")
    print("--------------------")
