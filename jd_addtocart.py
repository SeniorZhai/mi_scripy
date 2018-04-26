from selenium import webdriver
import pickle
import time

chrome=webdriver.Chrome()
cookies = pickle.load(open("jdcookies.pkl","rb"))
chrome.get(url="https://cart.jd.com/")
for cookie in cookies:
    chrome.add_cookie(cookie)
chrome.get(url="https://cart.jd.com/")
#times = time.strftime('%H:%M:%S',time.localtime(time.time()))
#print(times)
while True:
    try:
        chrome.get(url="cart.jd.com/gate.action?pid=6735798&pcount=1&ptype=1")
    except Exception:
        print("failed")
    time.sleep(1)
