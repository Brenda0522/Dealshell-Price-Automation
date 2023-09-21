import json
with open("next_page_url.json", "r") as next_page_url_file:
    next_page_url_data = json.load(next_page_url_file)
    for item in next_page_url_data:

        item_length = len(item.get("next_url"))
        print(item_length)
