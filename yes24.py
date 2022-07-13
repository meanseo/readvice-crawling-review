from cmath import exp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import pandas as pd


import time

import urllib3
import re

def remove_html(sentence) :
	sentence = re.sub('(<([^>]+)>)|\n|\t|&nbsp;|&amp;|&gt;', '', sentence)
	return sentence

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:\chromedriver.exe", options=options)
url = "http://www.yes24.com/24/Category/BestSeller"
driver.get(url)
# driver.maximize_window()

'''
경제/경영 3, 만화/라이트노벨 6, 소설/시/희곡 8, 어린이 10, 에세이 11, 여행 12, 
유아 15, 자기계발 18, IT 모바일 24
'''
categoreis = [18, 24]
review_list3 = []
review_list6 = []
review_list8 = []
review_list10 = []
review_list11 = []

# 장르 클릭
for category in categoreis:
    driver.find_element(By.XPATH,f'/html/body/div/div[2]/div[1]/div[1]/ul/li[1]/ul/li[{category}]/a').click()      
    time.sleep(2)
    # 페이지 클릭
    for page in range(1, 4):
        driver.find_element(By.XPATH,f'//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[{page}]').click()                                   
        time.sleep(2)
        # 도서 클릭
        for book in range(3, 40, 2):
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="category_layout"]/tbody/tr[{book}]/td[3]/p[1]/a[1]'))).click()
            for i in range(2, 7):
                try:
                    # 더보기 클릭
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="infoset_reviewContentList"]/div[{i}]/div[2]/a/div/span'))).click()
                    # 리뷰 가져오기                                                                                     
                    
                    review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="infoset_reviewContentList"]/div[{i}]/div[3]/div[2]'))).get_attribute("innerHTML")
                    # review = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="infoset_oneCommentList"]/div[3]/div[{i}]/div[1]/div[2]/span'))).get_attribute("innerHTML")
                    sentence = remove_html(review)
                    review_listi .append(sentence)
                    print(f'{review_list}\n')
                except:
                    continue
            driver.back()
    pd.DataFrame(review_list).to_csv(f'save/{category}_reivews.csv', index=False)
