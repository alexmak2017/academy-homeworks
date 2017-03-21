from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os
import time
import csv
geckodriver = os.path.join(os.path.dirname(os.path.abspath(__file__)),"geckodriver")
os.environ["webdriver.mozilla.driver"] = geckodriver

driver = webdriver.Firefox(geckodriver)
driver.get("http://toster.ru")

#1
search_input = driver.find_element_by_name("q")
search_input.send_keys("django"+Keys.RETURN)

#2-6
def parser():
    questions = driver.find_elements_by_class_name("question_short")
    for question in questions:
        title = question.find_element_by_class_name("question__title-link").text
        subscribers = question.find_element_by_class_name("question__views-count").text.split()[0]
        published = question.find_element_by_class_name("question__date_publish").get_attribute("datetime")

        try:
            question.find_element_by_class_name("icon_check")

            is_answer = True
        except NoSuchElementException:
            is_answer = False
        return (title, subscribers, published, is_answer)

#3-6
a = True
count = driver.find_elements_by_class_name("paginator__item-link")
for i in range(1,len(count)+1):

    if a:
        try:
            print(parser())
            next_page = driver.find_element_by_class_name("next").click()
        except NoSuchElementException:
            a = False
            print("last page")
        time.sleep(5)

#4
driver.set_window_size(414, 736)


driver = webdriver.Firefox(geckodriver)
driver.get("http://toster.ru")
ques = driver.find_elements_by_class_name("question__title-link")

#write to csv file:
"""
file_csv = open("example.csv", "a", encoding='utf-8')
csv_writer = csv.DictWriter(file_csv, fieldnames=["views", "content", "tags"], delimiter=",")
csv_writer.writeheader()

for que in ques:
    
    new_driver = webdriver.Firefox(geckodriver)
    link = que.get_attribute("href")
    new_driver.get(link)
    
    views = new_driver.find_element_by_class_name("question__views-count").text
    tags = new_driver.find_element_by_class_name("tags-list").text
    content = new_driver.find_element_by_class_name("question__text").text

    csv_writer.writerow({"views": views,
                         "content": content,
                         "tags": tags})

    new_driver.quit()
    time.sleep(15)

file_csv.close()
"""
#5
for que in ques:
    new_driver = webdriver.Firefox(geckodriver)
    link = que.get_attribute("href")
    new_driver.get(link)
    views = new_driver.find_element_by_class_name("question__views-count").text
    tags = new_driver.find_element_by_class_name("tags-list").text
    content = new_driver.find_element_by_class_name("question__text").text
    print(views, "\n", content, tags)
    new_driver.quit()
    time.sleep(1)


