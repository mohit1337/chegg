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
parser.add_argument('-u','--username', help='Username', required=True)
parser.add_argument('-p','--password', help='Password', required=True)
args = vars(parser.parse_args())

# Constants
login_url = "https://expert.chegg.com/expertqna"

chromedriver = join(dirname(abspath(__file__)),"drivers", "chromedriver.exe")
print(chromedriver)
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get(login_url)

def run_bot():
    """Login"""

    login = Login(driver)
    login.do_login(args['username'], args['password'])

    """Move to qna page"""


if __name__=="main":
    run_bot()
