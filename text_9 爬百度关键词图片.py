import re
import requests
from urllib import error
import os
num = 0


def dowmloadPicture(html, keyword):         #用来找到和下载图片
    global num               #全局变量
    pic_url = re.findall('"objURL":"(.*?)"', html, re.S)
    # 先利用正则表达式找到图片url  # re.findall(正则表达式,需要处理的字符串,说明匹配模式)
    #(.*?)‘.’代表任意字符；‘*?’非贪婪模式匹配(匹配越少越好)  ()代表输出括号内容，无括号和前后一起输出
    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:    #如果 each 不是空
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:                      #当没有异常发生时，else中的语句将会被执行
            string = file + r'\\' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return


if __name__ == '__main__':  # 主函数入口
    word = input("请输入搜索关键词(可以是人名，地名等): ")
    # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    numPicture = int(input('请输入想要下载的图片数量：'))
    file = input('请建立一个存储图片的文件夹，输入文件夹名称即可：')
    while os.path.exists(file) == 1:        #判断括号里的文件是否存在
        print('该文件已存在，请重新输入')
        file = input('请建立一个存储图片的文件夹，输入文件夹名称即可：')
    os.mkdir(file)                        #创建文件夹
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)     #timeout 设置连接超时的时间
            print(url)
        except error.HTTPError:
            print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            dowmloadPicture(result.text,word)
            t = t + 60

    print('当前搜索结束，感谢使用')
