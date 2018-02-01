import os
import requests
import re

url = "http://www.polypm.com.cn/index.php?s=Auction/workspic/pzid/PZ2036857/tp/0/np/"

if __name__ == '__main__':
    ret = requests.get(url)
    if ret.status_code == 200:
        print(ret.text)
    else:
        print('打开页面失败：',ret.status_code)
    