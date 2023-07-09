import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pageCrawl(driver):
    article_title = []
    article_link = []
    article_text = []

    try:
        article_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.list_news li"))
        )
        for article in article_list:
            try:
                news_info = article.find_element(By.CSS_SELECTOR, "div div a.news_tit")
                news_text = article.find_element(By.CSS_SELECTOR, "div div div.news_dsc div a")
                title = news_info.get_attribute('title')
                link = news_info.get_attribute('href')
                article_title.append(title)
                article_link.append(link)
                article_text.append(news_text.text)
            except:
                print("Error while parsing article")

    except:
        print("Error while fetching article list")

    return article_title, article_link, article_text


def start(title):
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news'

    article_title = []
    article_link = []
    article_text = []

    chrome_driver = os.path.join('chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.get(url)

    ele = driver.find_element(By.CSS_SELECTOR, '#nx_query')
    ele.send_keys(title)
    ele.submit()

    try:
        news_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#snb > div:nth-child(1) > div > div:nth-child(1) > a:nth-child(2)'))
        )
        news_button.click()

        article_title, article_link, article_text = pageCrawl(driver)

    except:
        print("Error while loading news page")

    driver.close()

    return article_title, article_link, article_text