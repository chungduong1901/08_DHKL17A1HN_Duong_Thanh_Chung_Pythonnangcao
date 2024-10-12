import json
def read_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def print_employee_statistics(data):
    company_name = data['company']['name']
    company_address = data['company']['address']
    departments = data['departments']

    total_employees = sum(department['employees'] for department in departments)

    print(f"Tên công ty: {company_name}")
    print(f"Địa chỉ: {company_address}")
    print("----- Thống kê nhân viên theo đơn vị -----")

    for index, department in enumerate(departments, start=1):
        department_name = department['name']
        employee_count = department['employees']
        percentage = (employee_count / total_employees) * 100
        print(f"{index}. Tên đơn vị: {department_name}")
        print(f"   - Số nhân viên: {employee_count}")
        print(f"   - Tỷ lệ: {percentage:.2f}%")
file_path = 'bai2.10.json' 
data = read_data_from_json(file_path)
print_employee_statistics(data)
