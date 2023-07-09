import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def pageCrawl(drive):
    article_title = []
    article_link = []
    article_list = drive.find_elements(By.XPATH, "//ul[@class=\"list_news\"]/li")
    for article in article_list:
        try:
            news_info = article.find_element(By.XPATH, "./div/div/a[@class=\"news_tit\"]")
            title = news_info.get_attribute('title')
            link = news_info.get_attribute('href')
            article_title.append(title)
            article_link.append(link)
        except:
            print("error")
    return article_title, article_link


def start(title):
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news'

    article_title = []
    article_link = []

    chrome_driver = os.path.join('chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # 브라우저 창을 표시하지 않도록 설정 (headless 모드)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    drive = webdriver.Chrome(chrome_driver, options=chrome_options)
    drive.get(url)

    ele = drive.find_element(By.XPATH, '//*[@id="nx_query"]')
    ele.send_keys(title)
    ele.submit()
    drive.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

    article_title, article_link = pageCrawl(drive)
    for i in range(len(article_title)):
        print(article_title[i])
        print(article_link[i])

    drive.close()

    return article_title, article_link