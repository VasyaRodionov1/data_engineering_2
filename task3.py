import json
import msgpack
import os
from collections import defaultdict

def aggregate_prices(products):
    aggregated_info = {}

    for product in products:
        name = product['name']
        price = product['price']

        if name not in aggregated_info:
            aggregated_info[name] = {'name': name, 'avg_price': 0, 'max_price': 0, 'min_price': float('inf')}

        aggregated_info[name]['avg_price'] = (aggregated_info[name]['avg_price'] + price) / 2
        aggregated_info[name]['max_price'] = max(aggregated_info[name]['max_price'], price)
        aggregated_info[name]['min_price'] = min(aggregated_info[name]['min_price'], price)

    return list(aggregated_info.values())

def save_to_json_and_msgpack(aggregated_info):
    json_file_path = 'result_task3.json'
    msgpack_file_path = 'result_task3.msgpack'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(aggregated_info, json_file, ensure_ascii=False, indent=2)

    with open(msgpack_file_path, 'wb') as msgpack_file:
        packed_data = msgpack.packb(aggregated_info, use_bin_type=True)
        msgpack_file.write(packed_data)

    return json_file_path, msgpack_file_path

def get_file_size(file_path):
    return os.path.getsize(file_path)

if __name__ == "__main__":
    with open('products_8_3.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    aggregated_info = aggregate_prices(data)
    json_file_path, msgpack_file_path = save_to_json_and_msgpack(aggregated_info)

    json_size = get_file_size(json_file_path)
    msgpack_size = get_file_size(msgpack_file_path)

    print(f'Size of JSON file: {json_size} bytes')
    print(f'Size of msgpack file: {msgpack_size} bytes')