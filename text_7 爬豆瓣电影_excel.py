import requests
from bs4 import BeautifulSoup
import xlwt                     #excel 模块
b = 1
a = 0

workbook = xlwt.Workbook(encoding = 'utf-8')    #打开一个 workbook (其实就是 excel )
worksheet = workbook.add_sheet('My Worksheet')  #创建表格

worksheet.write(0,1,"豆瓣电影top250")            #把内容写到表格第 i 行 j 列里
worksheet.write(1,0,"排名")
worksheet.write(1,1,"电影名")
worksheet.write(1,2,"评分")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

while a < 226:
    html = requests.get("https://movie.douban.com/top250?start={0}&filter=".format(a),headers=headers).text #访问反爬虫网页
    a += 25
    # print(html)
    soup = BeautifulSoup(html,features="lxml")     #网页解析为 lxml 格式
    all_a = soup.find_all("a", attrs={""})
    for j in all_a:
        b += 1
        html1 = j.get("href")       #得到 j 中 href 的属性
        # print(html1)
        html2 = requests.get(html1,headers=headers).text
        # print(html2)
        soup1 = BeautifulSoup(html2, features="lxml")
        try:
            top250 = soup1.find("span", attrs={"class": "top250-no"}).text
        except AttributeError:
            worksheet.write(b, 0,"页面不存在")
            continue
        # title = soup1.find("span", attrs={"property": "v:itemreviewed"}).text
        title1 = j.find("span", attrs={"class": "title"}).text
        scoring = soup1.find("strong", attrs={"class": "ll rating_num"}).text
        info = soup1.find("div", attrs={"id": "info"}).text

        worksheet.write(b,0, top250)
        worksheet.write(b,1, title1)
        worksheet.write(b,2, scoring)
        workbook.save('豆瓣电影top250.xls')       #保存表格为