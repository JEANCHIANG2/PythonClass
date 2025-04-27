import urllib.request as req
def getDate(url):
    # url='https://www.ptt.cc/bbs/movie/index10546.html'
    request = req.Request(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    # print(data)

    import bs4
    root = bs4.BeautifulSoup(data,'html.parser')
    #print(root.a.string)
    # titles=root.find_all('div',class_='title')
    # for title in titles:
    #     print(title.a.string)
    items = root.find_all('div', class_='r-ent')
    for item in items:
        title = item.find('div', class_='title')
        date = item.find('div', class_='date')
        nrec = item.find('span', class_='hl')
        author = item.find('div',class_='author')
        if nrec is None:
            nrec = '0'
        else:
            nrec =nrec.string
        if title.a is None:
            title = '本文已刪除'
        else:
            title = title.a.string

        print(f'{nrec:6} / {title:40} / {date.string:5}------{author.string:20}')
    nextPage = root.find('a',string='‹ 上頁')
    print(nextPage['href'])
pageURL ='https://www.ptt.cc/bbs/movie/index10546.html'
count = 0
while count < 3:
    pageURL =getData()
getDate('https://www.ptt.cc/bbs/movie/index.html')
