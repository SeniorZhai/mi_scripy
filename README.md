# 环境配置
1. `pip install selenium`
2. 修改`jd_getcookie`,`xm_getcookie`内的账号密码

# 说明
本项目基于selenium+chromedriver

jd,jd_addtocart,jd_getcookie为京东网页版实现
xm,xm_addtocart,xm_getcookie为小米商城实现

# 使用
京东实现需要先用jd_getcookie获取cookie
使用自己的账户名密码修改getcookies的定义
然后运行addtocart添加至购物车,jd_addtocart会以1.5s为时间间隔添加,请反复确认cookie可使用性
在运行addtocart的同时请将jd.py也同时运行
jd.py会反复提交购物车勾选的商品并提交订单

小米实现只需要在对应的三个文件中修改好账户名和密码即可
如果需要填写验证码请参考京东实现获取cookie再添加cookie进行访问
addtocart与xm.py的作用参考京东实现
```
python jd_getcookie.py
python jd_addtocart.py
python jd.py
```
