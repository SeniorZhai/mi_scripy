from selenium import webdriver
import time

xm_up={"ue":"159xxxx5347","pd":"xxxx"}


chrome=webdriver.Chrome()
chrome.get(url="https:////order.mi.com/site/login?redirectUrl=https://item.mi.com/product/10000085.html")
chrome.find_element_by_id("username").click()
User=chrome.find_element_by_id("username")
User.clear()
User.send_keys(xm_up["ue"])
Passwd=chrome.find_element_by_id("pwd")
Passwd.clear()
Passwd.send_keys(xm_up["pd"])
chrome.find_element_by_id("login-button").click()
time.sleep(1)
chrome.get(url="https://item.mi.com/product/10000085.html")
while True:
    try:
        chrome.get(url="https://item.mi.com/product/10000085.html")
        time.sleep(0.6)
        chrome.find_element_by_xpath("//*[@id=\"J_list\"]/div[1]/ul/li[3]/a/span[1]").click()
        time.sleep(0.6)
        chrome.find_element_by_xpath("//*[@id=\"J_buyBtnBox\"]/li/a").click()
        print("OK")
    except Exception:
        print("failed")
