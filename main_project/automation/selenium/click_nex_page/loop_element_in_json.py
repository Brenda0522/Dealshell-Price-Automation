import json

class Next_Page_Clicking:
    def __init__(self, web_url,next_page_path):
        self.web_url = web_url
        self.next_page_path = next_page_path

    @classmethod
    def get_dynamic_website(cls):
        with open("/Users/quangpham/Documents/my_project_aug_2023/project/main_project/main_project/list_data.json", 'r') as json_file:
            json_data = json.load(json_file)
            for website_data in json_data:
                if website_data.get("dynamic_website") == True:
                    web_url = website_data.get("start_url")
                    next_page_path = website_data.get("next_page_path")
                    return cls(web_url,next_page_path)
                else:
                    pass