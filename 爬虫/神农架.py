import requests
from bs4 import BeautifulSoup
import urllib


def download_images(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 解析HTML页面，提取图片链接
    image_tags = soup.find_all('img')
    for tag in image_tags:
        image_url = tag['src']

        # 下载图片
        urllib.request.urlretrieve(image_url, image_url.split('/')[-1])


# 示例：爬取神农架自然景观的图片链接
url = 'https://eee.xyly01.cn/m6kcegbk65gf/9774.html?plan=%E6%81%A9%E6%96%BD%E6%97%85%E6%B8%B82&unit=%E6%81%A9%E6%96%BD%E5%BF%85%E7%8E%A9%E6%99%AF%E7%82%B9&keyword=%E7%A5%9E%E5%86%9C%E6%9E%B6%E6%97%85%E6%B8%B8%E6%99%AF%E5%8C%BA%E5%AE%98%E7%BD%91&e_creative=77161383582&e_keywordid=625644324876&bd_vid=8059532858640029374'
download_images(url)
