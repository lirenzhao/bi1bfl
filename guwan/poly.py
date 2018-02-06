import os
import requests
import re

url = "http://www.polypm.com.cn/index.php?s=Auction/workspic/pzid/PZ2036857/tp/0/order//order_sc//np/"

def downPage(url):
    ret = requests.get(url)
    if ret.status_code == 200:
        html = ret.text.replace(' ',' ')
        #<strong class="workName"><a href="index.php?s=Auction/view/ppcd/art5120830001" target="_blank">明 青花瓜果纹罐</a></strong><br />
        a = re.findall('<strong class="workName"><a href="(.*?)".*?>(.*?)</a>',html)
        #<p class="work_p">
        #b = re.findall('<p class="work_p">(.*?)<br />',html)
        for i in a:
            #http://www.polypm.com.cn/index.php?s=Auction/view/ppcd/art5120830007
            art_url = "http://www.polypm.com.cn/" + i[0]
            print(art_url)
            art_ret = requests.get(art_url)
            if art_ret.status_code == 200:
                art_html = art_ret.text
                #<a href="http://auction3.img.artimg.net/auctionBigImage/art5120830001/2000-2000-b.jpg" class="jqzoom" rel='gal1' title="triumph" id="jqzoom1">
                art_img = re.findall('<a href="(.*?)" class="jqzoom"',art_html)[0]
                #art_img = art_info[0]
                print(art_img)
                # img = requests.get(art_img)
                # if img.status_code == 200:
                #     filename = "./images/" + art_img.split("/")[-2] + ".jpg"
                    
                #     with open(filename,'wb') as f:
                #         f.write(img.content)

                #     print('save image file ',filename)    
                # else:
                #     print('下载图片失败')
#<div class="show_title"><a href="javascript:void(0)"> 0007  清 青花山水盘、碗 （共三件）                   </a></div>
                art_info = re.findall('<div class="show_title">.*?>(.*?)</a>',art_html)
                
                print('art_info:',art_info[0].strip())

                art_html = art_html.replace(' ','').replace('\n','')
                
                art_info = re.findall('<li>成交价：.*?RMB(.*?)<!--',art_html)
                print('art_info:',art_info)

                art_info = re.findall('<li>类　别：.*?(.*?)</li',art_html)
                print('art_info:',art_info)

                # art_info = re.findall('<li>尺　　寸：.*?(.*?)</li',art_html)
                # print('art_info:',art_info)

                # art_info = re.findall('<li>创作年代：.*?(.*?)</li',art_html)
                # print('art_info:',art_info)

                # art_info = re.findall('<li>估　　价：.*?(.*?)</li',art_html)
                # print('art_info:',art_info)

                art_info = re.findall('<divclass="showTxt_bighidden"><br/>(.*?)<br/><br>(.*?)&nbsp;<br>(.*?)<divclass="close">',art_html)
                print('art_info:',art_info)

                art_info = re.findall('<li>尺　　寸：.*?(.*?)</li.*?<li>创作年代：.*?(.*?)</li.*?<li>估　　价：.*?(.*?)</li',art_html)
                print('art_info:',art_info)

                
            else:
                print('',art_ret.status_code)
            #break
        #print(ret.text)
        #for j in b:
        #    print(j)
        #print(len(b))
    else:
        print('打开页面失败：',ret.status_code)

if __name__ == '__main__':
    for i in range(1,100):
        page_url = url + str(i * 30)
        print(page_url)
        downPage(page_url)
        break