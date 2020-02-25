import requests
import re
from pyquery import PyQuery as pq
import time
# 猫眼实时抓取当日Top100榜单
# 相应请求
def main(link):
    url = link
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    commer = requests.get(url, headers=headers).text
    time.sleep(2) #防止网站出现验证问题等待
    html = pq(commer)
    word_processor(html)
# 清洗数据
def word_processor(html):
    img_name_souc = html(".board-img")
    book_name_souc = html(".name")
    img_name = re.findall(r'.*?data-src="(.*?)".*?', str(img_name_souc), re.S)
    book_name = re.findall(r'.*?title="(.*?)".*?', str(book_name_souc), re.S)
    write_flid(book_name, img_name)
# 写入数据到文件
def write_flid(book_name, img_name):
    flid = open("猫眼100爬取.txt", "a+")
    print(book_name, img_name)
    for i, m in zip(book_name, img_name):
        temp = (i, ":", m)
        flid.write(str(temp))
        flid.write("\n")
# 获取当前的地址并翻页
def link_next():
    for i in range(0, 100, 10):
        link = "https://maoyan.com/board/4?offset=%s" % i
        print("正在爬取第%s页" % i)
        if i == 90:
            print("爬取结束：猫眼100")
        main(link)
if __name__ == '__main__':
    link_next()