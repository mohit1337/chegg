#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Standard imports
from os.path import join, dirname, abspath
import argparse

# Third party imports
from selenium import webdriver

# Library imports
from pages.loginPage import Login

parser = argparse.ArgumentParser(description='Run chegg bot')
parser.add_argument('-u', '--username', help='Username', required=True)
parser.add_argument('-p', '--password', help='Password', required=True)
args = vars(parser.parse_args())

# Constants
login_url = "https://expert.chegg.com/expertqna"

chromedriver = join(dirname(abspath(__file__)), "drivers", "chromedriver.exe")
#geckodriver = join(dirname(abspath(__file__)), "drivers", "geckodriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=chromedriver)
#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
#driver = webdriver.Firefox(options=options, executable_path=geckodriver)
driver.maximize_window()
driver.get(login_url)


def run_bot():
    """Login"""

    login = Login(driver)
    login.do_login(args['username'], args['password'])

    """Move to qna page"""


if __name__ == "__main__":
    run_bot()
