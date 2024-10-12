import json
from datetime import datetime
def write_transactions_to_json(transactions):
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{current_time}.json"
    
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)
    
    print(f"Dữ liệu giao dịch đã được ghi vào tập tin {file_name}.")
def main():
    transactions = [
        {"type": "gold", "amount": 100, "value": 5000000},
        {"type": "money", "amount": 2000, "value": 2000000}
    ]
    
    user_input = input("Bạn có muốn ghi giao dịch vào tập tin? (1: Có, 0: Không): ")
    
    if user_input == '1':
        write_transactions_to_json(transactions)
    else:
        print("Không ghi dữ liệu vào tập tin.")
if __name__ == "__main__":
    main()
