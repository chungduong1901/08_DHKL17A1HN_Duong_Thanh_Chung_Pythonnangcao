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
chuoi_json = json.dumps(doi_tuong_python, indent=4, ensure_ascii=False)
print("Chuỗi JSON:")
print(chuoi_json)