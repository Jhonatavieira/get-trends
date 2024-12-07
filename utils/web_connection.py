from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# ROOT_FOLDER = Path(__file__).parent

# https://peter.sh/experiments/chromium-command-line-switches/


# When the function start with 'MAKE' --> This is an factory,
# just return the object"""


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    """INSERT DOCSTRING"""

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver
