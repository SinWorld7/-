from selenium import webdriver
from test_web import search_key
import test_data

web = webdriver.Edge()
web.implicitly_wait(5)

url = test_data.url["url"]
username = test_data.login_data["username"]
password = test_data.login_data["password"]
s_key = test_data.s_key["search_key"]
# print(url, username, password, s_key)
result = search_key(url=url, web=web, username=username, password=password, search_key=s_key)
print(result)
if s_key in result:
    print("搜索结果是正确的")
else:
    print("搜索结果是错误的")