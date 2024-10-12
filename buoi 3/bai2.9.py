import json

doi_tuong_python = {
    "ten": "ChungDuong",
    "tuoi": 20,
    "thanh_pho": "Ha Noi",
    "la_sinh_vien": True,
    "diem_so": [8, 9, 8],
    "dia_chi": {
        "duong": "abc",
        "so_nha": 123
    }
}
doi_tuong_sap_xep = dict(sorted(doi_tuong_python.items()))

chuoi_json = json.dumps(doi_tuong_sap_xep, indent=4, ensure_ascii=False)
print("Chuỗi JSON sau khi sắp xếp theo khóa và thụt lề 4:")
print(chuoi_json)