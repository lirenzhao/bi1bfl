#!/usr/bin/python3

import re
import requests
import os
import urllib
import pymysql
import db
import dict
import time

url = 'http://www.shufazidian.com'

sort = [("8","行书"),("9","楷书"),("7","草书"),("6","隶书"),("5","魏碑"),("4","简牍"),("3","篆书"),("shiliang","设计"),("zhuangke","篆刻")]

def save_img(img_url,file_name,file_path,title):
    try:
        if not os.path.exists(file_path):
            print('文件夹',file_path,'不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)
        file_suffix = os.path.splitext(img_url)[1]#获得图片后缀
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)#拼接图片名（包含路径）
        ret = requests.get(img_url) #下载图片，并保存到文件夹中
        if ret.status_code == 200:
            print('下载文件:',img_url)
            with open(filename,'wb') as f:
                f.write(ret.content)
            print('下载图片完成:',filename)
        else:
            print('下载图片失败')
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误 ：',e)

def getdown(word):
    count = 0
    for s in sort:
        data={'wd':word,'sort':s[0]}
        ret = requests.post(url,data)
        if ret.status_code == 200:
            print(data)
            ret.encoding='utf-8'
            html = ret.text.replace(' ','')
            a = re.findall('<arel="example_group"href="(http://.*?)"title="(.*?)"><img',html)            
            for i in a:
                file_path = './images/{}/{}'.format(data['wd'],s[1])
                title = i[1]
                img_url = i[0]
                save_img(img_url,str(count),file_path,title)
                
                file_suffix = os.path.splitext(img_url)[1]#获得图片后缀
                file_name = '{}{}{}{}'.format(file_path,'/',str(count),file_suffix)#拼接图片名（包含路径）
                shufa = {
                    'font':data['wd'],
                    'cate':s[1],
                    'title':title,
                    'images':file_name,
                }
                db.insert2('shufa_font',shufa)
                count = count + 1
                time.sleep(0.1)
            db.insert2_commit()
        else:
            print(ret.status_code)
    
    print('{} 书法字典图片下载完成'.format(word))

if __name__ == '__main__':

    try:
        for w in dict.dicts:
            getdown(w)
            print(w)
            time.sleep(0.2)
        db.insert2_close()
    except Exception as e:
        print(e)


    

