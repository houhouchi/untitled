from time import sleep
import os
import unittest
from appium import webdriver



# def setUp(self):
    # set up appium
    #app= os.path.abspath("")
app = os.path.join(os.path.dirname(__file__),'/Users/linran/Desktop/iOS包/test/huxiu.zip')
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wb/hub',
    desired_capabilities={
        'app':app,
        'paltformName': 'ios',
        'platformVersion': '9.4',
        'deviceName': 'iPhone 6'
     })
# def tearDown(self):
#     self.driver.quit()
