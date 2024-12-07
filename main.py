
"""TODO
"""
from utils.web_connection import make_chrome_browser
from selenium.webdriver.common.keys import Keys
# from utils.tags import web_driver_options
from utils import tags


URL = "https://bhissdigital.pbh.gov.br/creditoIPTU/apropriarCredito.jsp"


class Main():
    """Whrite
    """

    def __init__(self, url):
        self.url = url

    def get_connection(self):
        options = tags.web_driver_options()
        driver = make_chrome_browser(*options)
        driver.get(self.url)

        search_credit = tags.wait_for_element_by_tag_name_selector(
            driver, "//*[@id='navbar']/ul/li[2]/a", 10)
        search_credit.send_key(Keys.ENTER)


if __name__ == '__main__':

    browser = Main(URL)
    browser.get_connection()

    # Select the ...

    # run.get("https://google.com.br")

    # options = ('--headless', '--disable-gpu')
    # browser = make_chrome_brower(*options)

    # url = "https://google.com.br"
    # driver = WebConnection.
    # print(driver)

    # driver.get("https://bhissdigital.pbh.gov.br/creditoIPTU/apropriarCredito.jsp")

    # search_input.send_keys("God is good")
    # search_input.send_keys(Keys.ENTER)

    # sleep(TIME_TO_WAIT)
