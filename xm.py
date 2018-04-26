from selenium import webdriver
import time

xm_up={"ue":"159xxxx5347","pd":"xxxx"}


chrome=webdriver.Chrome()
chrome.get("https://order.mi.com/buy/checkout")
chrome.find_element_by_id("username").click()
User=chrome.find_element_by_id("username")
User.clear()
User.send_keys(xm_up["ue"])
Passwd=chrome.find_element_by_id("pwd")
Passwd.clear()
Passwd.send_keys(xm_up["pd"])
chrome.find_element_by_id("login-button").click()
time.sleep(0.5)
while True:
    try:
        chrome.get("https://order.mi.com/buy/checkout")
        chrome.find_element_by_xpath("//*[@id=\"J_addressList\"]/div[1]").click()
        chrome.find_element_by_xpath("//*[@id=\"J_checkoutToPay\"]").click()
    except Exception:
        print("failed")
