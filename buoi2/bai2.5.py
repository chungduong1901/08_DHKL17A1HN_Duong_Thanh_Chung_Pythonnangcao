from xml.dom import minidom
doc = minidom.parse('sample.xml')
danh_sach_nhan_vien = doc.getElementsByTagName('staff')
for nhan_vien in danh_sach_nhan_vien:
    ten = nhan_vien.getElementsByTagName('name')[0].firstChild.data 
    print("Tên nhân viên:", ten)
