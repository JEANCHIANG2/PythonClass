import urllib.request as req
url ='https://www.ptt.cc/bbs/gossiping/index.html'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}
data =req.Request(url, headers = header)
with req.urlopen(data) as response:
    data=response.read().decode('utf-8')
print(data)
