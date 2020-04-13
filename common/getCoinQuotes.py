import requests

# 爬取行情数据

class Coin():
    def __init__(self):
        self.url = "https://fxhapi.feixiaohao.com/public/v1/ticker?limit=10"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        self.proxies = {
            "http": "http://117.88.5.62:3000",
            "http": "http://121.237.149.11:3000",
            "http": "http://121.237.149.19:3000",
        }
    def getCoinList(self):
        page = requests.get(
            url=self.url, headers=self.headers, proxies=self.proxies)
        res = page.json()
        return res

