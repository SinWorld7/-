import selenium
# web 网站测试工具
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 把对应浏览器的驱动exe文件直接放在python的script文件夹下
# web = webdriver.Edge()
# web.get("http://120.78.128.25:8765")
# 跳到对应网址
# web.get("https://4399.com")
# web.maximize_window()
# 强制等待2s
# time.sleep(2)
# 隐式等待，最多10s，可提前
# 隐式等待全局生效，所以写在代码前面就好 注意：有一些页面是不执行隐式等待的（页面没加载出来），需要time.sleep()
# web.implicitly_wait(10)
# 后退
# web.back()
# 前进
# web.forward()
# 刷新
# web.refresh()


# 找关键字
# web.find_element_by_name()
# 找到name是k的框，发送植物大战僵尸的关键字
# web.find_element(by=By.NAME, value="k").send_keys("植物大战僵尸")
# time.sleep(5)
# web.find_element(by=By.CLASS_NAME, value="s_btn").click()
# time.sleep(5)
# web.find_element(by=By.CLASS_NAME, value="spec fr").find_element(by=By.CLASS_NAME, value="p_game").click()
# time.sleep(5)
# 找到标签属性是a的标签，找到其中文本是开始游戏的标签，点击
# web.find_element(by=By.XPATH, value="//a[@href='//www.4399.com/flash/18012.htm#search3-b962']").click()
# web.find_element(by=By.XPATH, value="//a[@one_click='send_log(18012,1,1,0);return true;']").click()
# <a onclick="send_log(18012,1,1,0);return true;" class="p_game" href="//www.4399.com/flash/18012.htm#search3-b962">开始游戏</a>

# 找到网页的标题，并输出
# web_title = web.title
# print(web_title)
# time.sleep(5)

# 识别是否有子页面的方式：
# 1 页面层级路径出现iframe,需要去切换iframe才可以进行元素的定位
# //iframe[@id="aaaaa" ]
# 2 切换找到iframe(iframe的id一直在变)
# id = web.find_element(by=By.Xpath, value="//iframe[@id='aaaaa']")
# web.switch_to.frame(id)
# 3 找不变的相关项来定位这个一直在变的,（/..代表这层标签的父标签, get_attribute(“XX”)得到标签的XX属性）,
# 假如父节点id不变，子id是父节点id拼接-frame
# fu_id = web.find_element(by=By.Xpath, value="//div[text()='零售出库']/..").get_attribute("id")
# zi_id = fu_id + "-frame"
# 第一种表达方式
# web.switch_to.frame(zi_id)
# 第二种表达方式
# web.find_element(by=By.Xpath, value="//iframe[@id='{}']").format(zi_id)
# 第三种表达方式（0是当前页面，1就是html下的次一级html，2是再次一级的html,再去找对应的id）
# 次一级html上面必定有一个iframe，iframe标志着次一级html的开始
# web.switch_to.frame(1)
# web.find_element(by=By.ID, value="searchNumber").send_keys("314")

# 退出，一般高版本的selenium会自动退出
# web.quit()


"""
 web自动化基本都是冒烟测试或者冒烟测试
 封装成函数能够更好地应用
"""

# 1 登陆账号密码
def login_page(username, password, web):
    web.find_element(by=By.ID, value="username").send_keys(username)
    web.find_element(by=By.ID, value="password").send_keys(password)
    web.find_element(by=By.ID, value='btnSubmit').click()
# 2 打开浏览器网址并让浏览器窗口最大化
def open_url(url, web):
    web.get(url)
    web.maximize_window()

# 3 最终封装
def search_key(url, web, username, password, search_key):
    open_url(url, web)
    login_page(username, password, web)
    web.find_element(by=By.XPATH, value="//span[text()='零售出库']").click()
    P_id = web.find_element(by=By.XPATH, value="//div[text()='零售出库']/..").get_attribute("id")
    F_id = P_id + "-frame"
    web.switch_to.frame(1)
    web.find_element(by=By.ID, value="searchNumber").send_keys(search_key)
    web.find_element(by=By.ID, value="searchBtn").click()
    time.sleep(1)
    num = web.find_element(by=By.XPATH, value="//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
    # if search_key in num:
    #     print("搜索结果是正确的")
    # else:
    #     print("搜索结果是错误的")



