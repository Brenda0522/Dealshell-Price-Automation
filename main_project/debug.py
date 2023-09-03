import json

with open('list_data.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        product_names = item.get('product_names')
        print(product_names)
