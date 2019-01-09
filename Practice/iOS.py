#coding=utf-8
from appium import webdriver

iosTest={}
iosTest['paltformName'] = 'ios'
iosTest['platVersion'] = '12.0'
iosTest['devicesName'] = 'iPhone 5'
iosTest['app'] = 'Users/linran/Desktop/Hoosho54cc.ipa'
d = webdriver.Remote('http://127.0.0.1:1473/wd/hub',iosTest)
