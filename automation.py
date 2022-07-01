from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_patients(search_parameters):
    
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=PATH, options=options)

    driver.get("http://demoserver99.com/assignments/index2.html")

    name_list = []

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="myTable_filter"]/label/input'))
    )

    for search_parameter in search_parameters:

        search_box.send_keys(search_parameter)
        
        containts = driver.find_elements(By.XPATH, '/html/body/div/div/table/tbody/tr')
        if len(containts) == 1:
            for containt in containts:
                if containt.text == "No matching records found":
                    name_list.append("")
                else:
                    td = containt.find_element(By.XPATH, '//tr/td[4]')
                    name_list.append(td.text.lower())

        else:
            for containt in containts:
                count = 0
                td = containt.find_elements(By.TAG_NAME, 'td')
                for detail in td:
                    if count == 4:
                        name_list.append(detail.text.lower())

        search_box.clear()
    driver.quit()
    
    return name_list
