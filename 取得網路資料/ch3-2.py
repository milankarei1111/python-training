# 匯入requests模組
import requests

# GET 簡易請求
response = requests.get("http://www.google.com")
print(response.status_code) # 取得請求狀態碼: 200

## 使用status_code屬性判斷請求狀態
if response.status_code == 200:
    print("請求成功")
else:
    print("請求失敗")

print("-------------------內建狀態碼---------------------------")

## requests.codes.ok 內建狀態碼
response = requests.get("http://www.google.com/404")
print(response.status_code) # 404
print(requests.codes.ok) #200
print(response.status_code == requests.codes.ok)

## requests.codes.all_good 內建狀態碼
response = requests.get("http://www.google.com/404")
print(response.status_code) # 404
print(requests.codes.all_good) #200
print(response.status_code == requests.codes.all_good)
#print(response.raise_for_status()) #  拋出requests.exceptions.HTTPError

# 3-2-1 GET 請求 , 傳參屬性:params , 格式: ?para1=value1&para2=value2
url_params = {'name':'陳會安', 'score':95}
get_response = requests.get("http://httpbin.org/get", params=url_params)
## url 取得網址，因為有中文字故會顯示URL編碼 http://httpbin.org/get?name=%E9%99%B3%E6%9C%83%E5%AE%89&score=95
print(get_response.url)
## text 取得回應字串
print(get_response.text)
## encoding 取得html編碼
print(get_response.encoding) #utf-8


# 3-2-2 POST 請求 , 傳參屬性:data
url = "http://httpbin.org/post"
post_params = {'name':'陳會安', 'score':95}
post_response = requests.post(url, data=post_params)
print(post_response.url)
print(post_response.text)

# 可使用httpbin網站的服務 請求/回應來測試

# 3-3-2 取得HTTP回應內容
url = "https://fchart.github.io/test.html"
content_response = requests.get(url)
print(content_response.text)
print("----------------------------------------------------")

## content 沒有編碼的位元組資料, 適用於非文字的請求
print(content_response.content)
print("----------------------------------------------------")

## raw 伺服器回應的原始Socket,回應HTTPResponse 物件
raw_response = requests.get(url, stream=True)
print(raw_response.raw)
print(raw_response.raw.read(15)) #指定讀取15個位元組

## json() 取得回應的json資料
url = "https://fchart.github.io/json/Example.json"
r = requests.get(url)
print(r.text)
print(type(r.text)) # <class 'str'>

print("----------------------------------------------------")
print(r.json())
print(type(r.json())) # <class 'dict'>


# 3-3-4 取得回應標頭資訊
print("------------------取得回應標頭資訊(一)---------------------")
response = requests.get("http://www.google.com")
print(response.headers["Content-Type"]) # text/html; charset=ISO-8859-1
print(response.headers["Content-Length"]) # 6815
print(response.headers["Date"]) # Mon, 14 Nov 2022 13:54:15 GMT
print(response.headers["Server"]) #gws => google web server

print("------------------取得回應標頭資訊(二)---------------------")
print(response.headers.get("Content-Type"))
print(response.headers.get("Content-Length"))
print(response.headers.get("Date"))
print(response.headers.get("Server"))