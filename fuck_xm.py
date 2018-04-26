#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import os
from selenium import webdriver

class SubscribeTel(object):
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        self.login_url = 'https://account.xiaomi.com/pass/serviceLogin'  # 小米登录网址
        self.login_sec = 'https://account.xiaomi.com/pass/auth/security/home'  # 小米登录成功后网址
        self.sub_url = 'https://item.mi.com/product/10000085.html'  # 小米mix 2s 网址
        self.driver_name = 'chrome'
        self.executable_path = os.getcwd()+'/geckodriver'

    def login(self):
        # 访问登录网址
        self.browser.get(self.login_url)
        # 填充用户名
        self.browser.find_element_by_name('user').send_keys(self.username)
        time.sleep(0.3)
        # 填充密码
        self.browser.find_element_by_name('password').send_keys(self.passwd)
        # 登录
        self.browser.find_element_by_id('login-button').click()
        # 循环等待登录，登录成功，跳出循环
        while True:
            if self.browser.current_url[:50] != self.login_sec:
                time.sleep(1)
            else:
                # logbticket.info("登陆成功...")
                print('登录成功...')
                break

    def start_sub(self):
        # 创建一个浏览器对象
        self.browser = webdriver.Chrome()
        # 设置窗口大小尺寸
        self.browser.set_window_size(1400, 1000)
        # 用户登录
        self.login()
        # 进入预购页面
        self.browser.get(self.sub_url)
        self.browser.implicitly_wait(2)
        if self.browser.find_element_by_xpath("//a[@data-name='立即预约']"):
            self.browser.find_element_by_xpath("//a[@data-name='立即预约']").click()
        # 选择内存
        self.browser.find_element_by_xpath("//li[@data-name='6GB+128GB']").click()
        # 选择颜色
        self.browser.find_element_by_xpath("//img[@alt='黑色']").click()
        while True:
            times = self.browser.find_element_by_xpath("//span[@class='time J_orderTime']").text
            if times == u'剩 00 时 00 分 00 秒':
                self.browser.find_element_by_xpath("//a[@data-name='加入购物车']").click()
                print('加入购物车成功...')
                break
            else:
                time.sleep(0.5)


if __name__ == '__main__':
    username = '****'
    passwd = '****'
    Tel = SubscribeTel(username, passwd)
    Tel.start_sub()

