
"""TODO
"""
from utils.web_connection import make_chrome_browser
from selenium.webdriver.common.keys import Keys
# from utils.tags import web_driver_options
from utils import functions
# from time import sleep


URL = "https://bhissdigital.pbh.gov.br/creditoIPTU/apropriarCredito.jsp"
ID = "id"
CLASS = "class"
XPATH = "xpath"


class Main():
    """Whrite
    """

    def __init__(self, url):
        self.url = url
        self.driver = "None"

    def run(self):
        """Start application"""
        options = functions.web_driver_options()
        self.driver = make_chrome_browser(*options)
        self.driver.get(self.url)
        
    def web_manipulation(self):

        search_credit = functions.find_element(
            self.driver, XPATH, "//*[@id='navbar']/ul/li[2]/a")
        search_credit.send_keys(Keys.ENTER)

        # Write the CPF on the lable     
        insert_cpf = functions.find_element(self.driver, ID, "CPF")
        insert_cpf.send_keys("01542287618")

        # Click on the button Credit Search
        credit_search = functions.find_element(self.driver, ID, "consultar")
        credit_search.send_keys(Keys.ENTER)

        # Find text 
        user_message = functions.find_element(self.driver, CLASS, "text-justify")
        text_infor = user_message.text
        print(text_infor)

        


if __name__ == '__main__':

    start = Main(URL)
    start.run()
    start.web_manipulation()

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
