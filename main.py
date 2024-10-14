from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


ROOT_FOLDER = Path(__file__).parent

# When the function start with "MAKE" --> This is an factory
# Just return the object


# https://peter.sh/experiments/chromium-command-line-switches/

def make_chrome_brower(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # options = ('--headless', '--disable-gpu')
    # browser = make_chrome_brower(*options)
    browser = make_chrome_brower()
    browser.get("http://google.com")

    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'APjFqb')
        )
    )

    search_input.send_keys("God is good")
    search_input.send_keys(Keys.ENTER)
    sleep(TIME_TO_WAIT)
