from urllib.request import Request, urlopen

def getJson():
    # zb网站获取数据Api
    url = "http://127.0.0.1:5000/api/test"
    # 包装头部
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # 构建请求
    request = Request(url, headers=firefox_headers)
    html = urlopen(request)
    # 获取数据
    data = html.read()
    # 转换成字符串
    strs = str(data)
    # 截取字符串
    strs_for_json = strs[5:]
    strs_for_json = strs_for_json[:-4]
    # 去除转义字符
    print(strs_for_json)
    strs_for_json = strs_for_json.replace('\\','')
    print(strs_for_json)
    #写入文件
    f = open('C:/Users/Administrator/Desktop/python/project_dataAnalysis/data.json', 'w')
    f.write(strs_for_json)
    f.close()
    return (strs_for_json)