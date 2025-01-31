from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from time import sleep

timeout = 2


def web_driver_options():
    options = [
        "--window-size=1366,768",
        "user-agent="
        "Mozilla/5.0 Windows NT 10.0; Win64;x64, AppleWebKit/537.36 KHTML, "
        "like Gecko,Chrome/88.0.4324.182 Safari/537.36"
        "--disable-blink-features=AutomationControlled",
        "--disable-extensions",
        "--proxy-server='direct://'",
        "--proxy-bypass-list=*",
        '--ignore-certificate-errors',
        "--password-store=basic",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--enable-automation",
        "--disable-browser-side-navigation",
        "--disable-web-security",
        "--disable-dev-shm-usage",
        "--disable-infobars",
        "--disable-gpu",
        "--disable-setuid-sandbox",
        "--disable-software-rasterizer",
    ]
    return options


locator_map = { 

    'id': By.ID, 
    'name': By.NAME, 
    'xpath': By.XPATH, 
    'class': By.CLASS_NAME
}

def find_element(driver, element, selector):
    try:
        locator = locator_map.get(element.lower())
        if locator:            
            return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator, selector)),
            'Could not find element with selector "{}"'.format(selector)
        )
        else:
            raise ValueError(f"Locator strategy '{element}' not supported.")
    except: 
        raise ValueError("Error during to find some element page")
