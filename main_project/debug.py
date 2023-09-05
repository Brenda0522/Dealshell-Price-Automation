import json

with open('list_data.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        product_names = item.get('current_product_url')
        current_product_url = item.get("current_product_url")
        products_url = item.get('products_url') + "/game-pokemon-scarlet-pokemon-violet-double-pack-us-nintendo-switch"
        print(products_url)