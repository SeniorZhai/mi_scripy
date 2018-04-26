from selenium import webdriver
import pickle
import time

xm_up={"ue":"***@**.com","pd":"******"}


chrome=webdriver.Chrome()
chrome.get(url="https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%253Fclient_id%253D180100041086%26sign%3DMzU2MGI1MjBiZWJhOTQyYTdmZmRhZDViM2NkMTFiMWQwZDAyMjE4ZQ%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180")
chrome.find_element_by_id("username").click()
User=chrome.find_element_by_id("username")
User.clear()
User.send_keys(xm_up["ue"])
Passwd=chrome.find_element_by_id("pwd")
Passwd.clear()
Passwd.send_keys(xm_up["pd"])
chrome.find_element_by_id("login-button").click();
time.sleep(1);
cookies = chrome.get_cookies()
pickle.dump(cookies,open("xmcookies.pkl","wb"))
