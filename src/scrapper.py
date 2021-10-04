from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        pass

    def __get_html(self, url, n):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        if n > 5:
            for i in range((n-1)//5):
                btn = driver.find_element(By.CLASS_NAME, 'sc-2nb8qo-0')
                down = driver.find_element_by_class_name("huqdoR")
                actions = ActionChains(driver)
                actions.move_to_element(down).click(btn).perform()
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'sc-2nb8qo-0'))
                )
        return driver.page_source

    def __get_content(self, html, n):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("div", class_="svowul-5", limit=n)
        news = []

        for item in items:
            news.append(
                {
                    'title': item.find("h3", class_="sc-1q9q90x-0").get_text(),
                    'source': item.find("span", class_="svowul-7").get_text(),
                    'time': item.find("span", class_="hykWbK").get_text()
                }
            )
        return news

    def grab(self, crypto, N):
        URL = 'https://coinmarketcap.com/currencies/' + crypto + '/news/'
        page = self.__get_html(URL, N)
        print(self.__get_content(page, N))
