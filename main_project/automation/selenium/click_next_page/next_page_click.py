import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .loop_element_in_json import Next_Page_Clicking
import json

class Page_clicker:
    with open("/Users/quangpham/Documents/my_project_aug_2023/project/main_project/main_project/automation/selenium/click_next_page/next_page_url.json", "w") as next_page_url:
        pass
    def __init__(self):
        self.current_url = ""
        self.url_list = []
    def get_url(self):
        current_url = self.current_url
        if current_url == "":
            get_page = Next_Page_Clicking.get_dynamic_website().web_url
            return get_page
        elif current_url != "":
            return current_url
    def automate_clicking_through_pages(self):
        url_list = self.url_list
        current_url = self.current_url  # 
        driver = webdriver.Chrome("")  # Add the path to your Chrome driver
        next_page_path = Next_Page_Clicking.get_dynamic_website().next_page_path
        while True:  # Infinite loop to keep clicking until the last page
            get_page = self.get_url()
            current_url = get_page
            url_list.append(current_url) # Append the current_url to url_list
            next_page_url = f"{current_url}"
            driver.get(next_page_url)
            try:
                element = driver.find_element(By.XPATH, f"{next_page_path}")
                element.click()
            except NoSuchElementException:
                url_list = self.double_quoted_list(url_list)
                self.save_to_json(url_list)
                break  # Exit the loop if the element is not found (last page)

            ##
            self.current_url = driver.current_url
            ##d

        driver.quit()

    # def upload_to_json():
    @staticmethod
    def save_to_json(current_url):
        with open("/Users/quangpham/Documents/my_project_aug_2023/project/main_project/main_project/automation/selenium/click_next_page/next_page_url.json", "a") as next_page_url:
            next_page_url.write(f'{current_url}')
    @staticmethod
    def double_quoted_list(input_list):
        # Create a new list where each item is enclosed in double quotes
        quoted_items = [f'"{item}"' for item in input_list]
        # Join the quoted items with commas and enclose them in square brackets
        formatted_str = f'[\n{{"next_url": [{",".join(quoted_items)}]}}\n]'
        return formatted_str
# find out how the code flow throught the programm and give one variable to store the url that the program is currently on then compare those two together and from that we could create a condition to break the infinite loop 
# im currently strugling with fixing the error that the program can not find the last page, because it canot find the last page so it up date the url data as a list into the json file. if the programe is error it will automaticly log out and won't letme save the data in to that file
# i've done it baby finally able to change all the single quote to double quote therefore i finally done with this fuction hâhhahahah, and i also learn how to do list comprehension which i could  loop in a single line (A list comprehension is a concise way to create a new list by applying an expression to each item in an existing iterable (e.g., a list, tuple, or string)).
#and now I create a class to use in spider. we are officilly done