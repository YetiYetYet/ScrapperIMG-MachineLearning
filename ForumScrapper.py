from selenium import webdriver
import os
import pandas as pd
import urllib
import urllib.request


def init_file(researched):
    path = os.getcwd()
    path += "/out/"

    os.makedirs(path, exist_ok=True)

    path += researched + "/"

    if os.path.isdir(path):
        cmd = "rm -rf " + path
        os.popen(cmd + ' 2>&1', 'r')

    os.makedirs(path, exist_ok=True)
    return path


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p702')

comments = pd.DataFrame(columns=['Date', 'user_id', 'comments'])
ids = driver.find_elements_by_xpath("//*[contains(@id,'Comment_')]")
