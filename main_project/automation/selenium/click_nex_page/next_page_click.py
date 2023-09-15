import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from loop_element_in_json import Next_Page_Clicking

current_url = ""

def get_url():
    if current_url == "":
        get_page = Next_Page_Clicking.get_dynamic_website().web_url
        return get_page
    elif current_url != "":
        return current_url

def automate_clicking():
    global current_url  # Declare current_url as a global variable
    driver = webdriver.Chrome("")  # Add the path to your Chrome driver
    next_page_path = Next_Page_Clicking.get_dynamic_website().next_page_path
    while True:  # Infinite loop to keep clicking until the last page
        get_page = get_url()
        current_url = get_page
        print(current_url) # this is where written the urls to another json file
        next_page_url = f"{get_page}"
        driver.get(next_page_url)
        element = driver.find_element(By.XPATH, f"{next_page_path}")
        element.click()
        current_url = driver.current_url
        # Check if you have reached the last page, you should modify this condition
        if current_url == None:
            break  # Exit the loop if it's the last page
    driver.quit()

# def upload_to_json():
automate_clicking()
